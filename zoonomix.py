import os
import pandas as pd
from Bio import SeqIO
import subprocess

# Define category weights and risk levels
CATEGORY_WEIGHTS = {
'Adherence': 6,
    'Biofilm': 4,
    'Efflux_pump': 4,
    'Exotoxin': 6,
    'Resistance': 4,
    'T3SS': 6,
    'T4SS': 5,
    'T6SS': 5,
    'Integrative_Conjugative_Element': 5,
    'ompA': 6,
    'superoxide_dismutase': 5,
    'capsular_polysaccharide_synthesis_enzyme_CapB': 5,
    'FimH_protein': 6,
    'phospholipase_D': 5,
    'toxin_A': 6,
    'pertussis_toxin_subunit_1': 6,
    'invA': 6,
    'lpxD': 6,
    'Filamentous_hemagglutinin-adhesin': 6,
    'mgtC': 5,
    'RNA_polymerase_sigma_factor_RpoS': 5
}

RISK_LEVELS = {
    "High Risk of pathogenicity and Zoonotic potential": lambda score: score >= 50,
    "Moderate Risk of pathogenicity and Zoonotic potential": lambda score: 30 <= score < 50,
    "Low Risk of pathogenicity and Zoonotic potential": lambda score: score < 30
}

# Add new genes and proteins for detection
DETECTION_GENES = [
    "ompA",
    "superoxide_dismutase",
    "capsular_polysaccharide_synthesis_enzyme_CapB",
    "FimH_protein",
    "phospholipase_D",
    "toxin_A",
    "pertussis_toxin_subunit_1",
    "invA",
    "lpxD",
    "Filamentous_hemagglutinin-adhesin",
    "mgtC",
    "RNA_polymerase_sigma_factor_RpoS",
    "Adherence",
    "Biofilm",
    "Exotoxin",
    "T3SS",
    "T4SS",
    "T6SS",
    "resfinder",
    "Resistance"
]

CATEGORY_MAPPING = {
    'ICEberg': 'Integrative_Conjugative_Element',
    'resfinder': 'Resistance',
    'PID': 'T4SS',
    'Efflux': 'Efflux_pump',
    'T6SS': 'T6SS',
    'T3SS': 'T3SS'  # Add explicit mapping for T3SS
}

def create_annotations_file(fasta_file, output_file):
    """Create annotations TSV file from a FASTA file with enhanced logic."""
    if os.path.exists(output_file):
        print(f"Annotations file already exists at {output_file}. Skipping regeneration.")
        return

    annotations = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq_id = record.id
        header = record.description
        category = "Unknown"

        # Debugging: Print headers being processed
        print(f"Processing sseqid: {seq_id}, Header: {header}")

        matched = False

        # Check for specific genes first (e.g., Resistance)
        for gene in DETECTION_GENES:
            if gene.lower() in header.lower():
                category = gene
                print(f"Matched DETECTION_GENES: {gene}")
                matched = True
                break

        # Check for broader categories if no specific gene matched
        if not matched:
            for keyword, cat in CATEGORY_MAPPING.items():
                if keyword.lower() in header.lower():
                    category = cat
                    print(f"Matched CATEGORY_MAPPING: {keyword} -> {category}")
                    matched = True
                    break

        if not matched:
            print(f"No match found for sseqid: {seq_id}")

        annotations.append((seq_id, category))

    # Save annotations
    with open(output_file, "w") as out_file:
        out_file.write("sseqid\tCategory\n")
        for seq_id, category in annotations:
            out_file.write(f"{seq_id}\t{category}\n")
    print(f"Annotations file saved to {output_file}")

def run_blast(query_file, db_path, output_file):
    """Run BLAST with enhanced sensitivity."""
    command = [
        "blastn",
        "-query", query_file,
        "-db", db_path,
        "-out", output_file,
        "-outfmt", "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore",
        "-evalue", "1e-5",  # Increased sensitivity
        "-perc_identity", "80"  # Allow matches with 80% identity or higher
    ]
    print(f"Running BLAST with command: {' '.join(command)}")
    subprocess.run(command, check=True)
    print(f"BLAST completed. Results saved to {output_file}.")

def parse_blast_results(blast_results_file, annotation_file):
    """Parse BLAST results, merge overlapping regions for ICEberg, and remove duplicates where qstart or qend are the same for all genes."""
    annotations = pd.read_excel(annotation_file)
    blast_results = pd.read_csv(blast_results_file, sep="\t", header=None, names=[
        "qseqid", "sseqid", "pident", "length", "mismatch", "gapopen",
        "qstart", "qend", "sstart", "send", "evalue", "bitscore"
    ])

    # Deduplicate entries by 'qseqid' and 'sseqid'
    blast_results = blast_results.drop_duplicates(subset=['qseqid', 'sseqid'])

    # Sort by qseqid and qstart for processing
    blast_results.sort_values(by=["qseqid", "qstart"], inplace=True)

    filtered_results = []
    for qseqid, group in blast_results.groupby("qseqid"):
        merged_intervals = []  # To track merged intervals for ICEberg
        processed_qstarts = set()  # Track all processed qstart values
        processed_qends = set()  # Track all processed qend values

        for _, row in group.iterrows():
            qstart, qend = row["qstart"], row["qend"]
            sseqid = row["sseqid"]

            # Skip if qstart or qend is already processed
            if qstart in processed_qstarts or qend in processed_qends:
                continue

            # Add qstart and qend to the processed sets
            processed_qstarts.add(qstart)
            processed_qends.add(qend)

            # Check if the sseqid belongs to ICEberg
            if "ICEberg" in sseqid:
                merged = False
                for interval in merged_intervals:
                    # If the interval overlaps with an existing one, merge them
                    if interval[0] <= qstart <= interval[1] or interval[0] <= qend <= interval[1]:
                        interval[0] = min(interval[0], qstart)
                        interval[1] = max(interval[1], qend)
                        merged = True
                        break
                if not merged:
                    # Add a new interval for ICEberg
                    merged_intervals.append([qstart, qend])
                else:
                    # Skip adding as it's merged
                    continue

            # Add the row to filtered results
            filtered_results.append(row)

    # Create a DataFrame from the filtered results
    filtered_results_df = pd.DataFrame(filtered_results)

    # Add query coverage filter (80-100%)
    filtered_results_df['query_coverage'] = (
        filtered_results_df['length'] / (filtered_results_df['qend'] - filtered_results_df['qstart'] + 1)) * 100
    filtered_results_df = filtered_results_df[
        (filtered_results_df['query_coverage'] >= 80) & (filtered_results_df['query_coverage'] <= 100)]

    # Merge with annotations
    merged = pd.merge(filtered_results_df, annotations, on="sseqid", how="left")

    # Debugging: Print merge summary
    print(f"Merged results:\n{merged.head()}\n")

    return merged



def calculate_scores_and_risks(results):
    """Calculate scores and risk levels."""
    category_counts = results['Category'].value_counts().to_dict()

    # Debugging: Print category counts
    print(f"Category counts: {category_counts}")

    total_score = sum(CATEGORY_WEIGHTS.get(category, 0) * count for category, count in category_counts.items())
    risk_level = next(level for level, condition in RISK_LEVELS.items() if condition(total_score))
    return category_counts, total_score, risk_level

def save_results_to_excel(high_identity_results, mid_identity_results, excel_path):
    """Save results and summary to an Excel file."""
    # Filter high-identity results (100% identity) and bit score > 750
    high_identity_results = high_identity_results[(high_identity_results['pident'] >= 99.99) & (high_identity_results['bitscore'] > 750)]

    with pd.ExcelWriter(excel_path) as writer:
        # Save Microbe Status (100% identity)
        high_identity_unique = high_identity_results.drop_duplicates(subset=['qstart', 'qend'])
        high_identity_unique.drop(columns=['Category'], inplace=True, errors='ignore')
        high_identity_unique.to_excel(writer, index=False, sheet_name="Microbe Status")

        # Save Future Mutation (95-99.99% identity) and bit score > 1000
        mid_identity_results = mid_identity_results[mid_identity_results['bitscore'] > 1000]
        mid_identity_unique = mid_identity_results.drop_duplicates(subset=['qstart', 'qend'])
        mid_identity_unique.drop(columns=['Category'], inplace=True, errors='ignore')
        mid_identity_unique.to_excel(writer, index=False, sheet_name="Future Mutation")

        # Create Gene Count sheet
        keywords = list(set(CATEGORY_MAPPING.keys()).union(DETECTION_GENES))  # Ensure unique keys
        gene_count_data = []

        for keyword in keywords:
            # Filter unique entries based on qstart and qend
            high_filtered = high_identity_unique[high_identity_unique['sseqid'].str.contains(keyword, case=False, na=False)]
            mid_filtered = mid_identity_unique[mid_identity_unique['sseqid'].str.contains(keyword, case=False, na=False)]

            current_count = len(high_filtered)
            future_count = len(mid_filtered)

            # Debugging: Print counts for each keyword
            print(f"Keyword: {keyword}, Current Count: {current_count}, Future Count: {future_count}")

            gene_count_data.append({
                "Gene/Category": CATEGORY_MAPPING.get(keyword, keyword),
                "Current Status": current_count,
                "Future Status": future_count
            })

        # Remove duplicates from the gene count data
        gene_count_df = pd.DataFrame(gene_count_data).groupby("Gene/Category", as_index=False).sum()
        gene_count_df.to_excel(writer, index=False, sheet_name="Gene Count")

        # Calculate Total Current Score from Gene Count
        total_current_score = sum(
            CATEGORY_WEIGHTS.get(row["Gene/Category"], 0) * row["Current Status"]
            for _, row in gene_count_df.iterrows()
        )

        # Calculate Future Score
        total_future_score = sum(
            CATEGORY_WEIGHTS.get(row["Gene/Category"], 0) * row["Future Status"]
            for _, row in gene_count_df.iterrows()
        )

        # Determine Risk Levels
        current_risk_level = next(level for level, condition in RISK_LEVELS.items() if condition(total_current_score))
        future_risk_level = next(level for level, condition in RISK_LEVELS.items() if condition(total_future_score))

        # Determine High Chance of Antibiotic Resistance Migration
        high_resistance_migration = (
            (gene_count_df.loc[gene_count_df["Gene/Category"] == "Integrative_Conjugative_Element", "Current Status"].sum() > 0) and
            (gene_count_df.loc[gene_count_df["Gene/Category"] == "Resistance", "Current Status"].sum() > 0) and
            (gene_count_df.loc[gene_count_df["Gene/Category"] == "T4SS", "Current Status"].sum() > 0)
        )

        # Write Summary
        summary_data = {
            "Total Current Score": total_current_score,
            "Current Risk Level": current_risk_level,
            "Total Future Score": total_future_score,
            "Future Risk Level": future_risk_level,
            "High Chance of Antibiotic Resistance Migration": "Yes" if high_resistance_migration else "No"
        }
        summary_df = pd.DataFrame([summary_data])
        summary_df.to_excel(writer, index=False, sheet_name="Summary")

        print("Gene Count and Summary sheets saved successfully.")


def main():
    query_file = r"C:\\Users\\Lenovo\\Desktop\\Zoonoticmap\\query_sequences.fasta"
    db_path = r"C:\\Users\\Lenovo\\Desktop\\Zoonoticmap\\reference_db"
    blast_results_file = r"C:\\Users\\Lenovo\\Desktop\\Zoonoticmap\\blast_results_annotated.tsv"
    annotation_file = r"C:\\Users\\Lenovo\\Desktop\\Zoonoticmap\\annotations_1.xlsx"
    final_excel = r"C:\\Users\\Lenovo\\Desktop\\Zoonoticmap\\final_results.xlsx"

    create_annotations_file(query_file, annotation_file)
    run_blast(query_file, db_path, blast_results_file)
    results = parse_blast_results(blast_results_file, annotation_file)

    high_identity_results = results[results['pident'] >= 99.99]
    mid_identity_results = results[(results['pident'] >= 95) & (results['pident'] < 99.99)]

    save_results_to_excel(high_identity_results, mid_identity_results, final_excel)
    print(f"Results saved to {final_excel}")

if __name__ == "__main__":
    main() 
