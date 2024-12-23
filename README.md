# ZoonomiX Pipeline

ZoonomiX is a comprehensive bioinformatics pipeline designed to analyze microbial genomes for identifying critical genes and predicting their roles in antibiotic resistance, virulence, pathogenicity, and zoonotic potential. Leveraging **BLASTn** and curated reference databases, ZoonomiX evaluates sequences to score future risks and adaptability of microbes.

---

## Features

- **Gene Identification**:
  - Detects genes linked to adherence, biofilm formation, efflux pumps, virulence factors, and more.
  - Supports custom and curated reference databases for enhanced accuracy.

- **Resistance and Pathogenicity Prediction**:
  - Identifies genes contributing to antibiotic resistance and virulence.
  - Scores microbes for their potential pathogenicity and zoonotic risk.

- **Comprehensive Analysis**:
  - Utilizes curated databases:
    - Adherence
    - Biofilm
    - Efflux Pumps
    - Exotoxins
    - Integrative and Conjugative Elements (ICEs)
    - Secretion Systems (T3SS, T4SS, T6SS)
    - Zoonotic Virulence Factors
  - Incorporates horizontal gene transfer (HGT) markers like ICEs and resistance elements.

- **Customizable Parameters**:
  - User-defined thresholds for BLASTn alignment:
    - E-value
    - Percent identity
    - Query coverage

- **Detailed Outputs**:
  - Tabular report with gene annotations, alignment statistics, and risk scores.
  - Summarized Excel file for easy interpretation.

---

## Reference Databases

ZoonomiX relies on curated FASTA reference databases:

| Database Name                | Number of Sequences | Description                                   |
|------------------------------|---------------------|-----------------------------------------------|
| Adherence_genes              | 5,201               | Genes related to microbial adherence.         |
| Biofilm_genes                | 814                 | Biofilm-related genes aiding persistence.     |
| Efflux_genes                 | 93                  | Efflux pump genes for multidrug resistance.   |
| Exotoxin_genes               | 1,324               | Genes encoding exotoxins.                     |
| ICE_genes                    | 1,326               | Genes linked to Integrative and Conjugative Elements. |
| Resistance_genes             | 3,151               | Known antibiotic resistance genes.           |
| T3SS_genes                   | 925                 | Genes for Type 3 Secretion Systems.          |
| T4SS_genes                   | 10,795              | Genes for Type 4 Secretion Systems.          |
| T6SS_genes                   | 1,411               | Genes for Type 6 Secretion Systems.          |
| Virulance_genes_Zoonotic     | 13                  | Zoonotic virulence factors.                  |

---

## Prerequisites

### 1. Hardware Requirements
- A computer with sufficient **RAM** and **storage** for bioinformatics tasks.
- Stable **internet connection** to download tools and databases.

### 2. Software Requirements

#### Python Environment
- **Python 3.8 or later**.
- Required Python Libraries:
  - `pandas`: For data manipulation and analysis.
  - `openpyxl`: For Excel file handling.
  - `biopython`: For biological sequence data processing.
- Install libraries using pip:
  ```bash
  pip install pandas openpyxl biopython

  **BLAST+ (Basic Local Alignment Search Tool)**
Download and install BLAST+ from the NCBI BLAST website.
Add BLAST executables (e.g., blastn, makeblastdb) to your system PATH.

### Test installation:
bash
Copy code
blastn -version
Spreadsheet Software
Microsoft Excel or alternatives like LibreOffice or Google Sheets to view output files.
Text Editor/IDE

### Recommended editors:
VSCode
PyCharm
Any plain text editor.

### Query Sequences File:
A properly formatted FASTA file containing microbial sequences (e.g., query_sequences.fasta).

### Reference Database:
A BLAST-compatible database created using makeblastdb from BLAST+.

### Optional Annotation File:
Excel file for mapping categories (e.g., annotations_1.xlsx).

### Output Files
Annotated Results:
.tsv file with BLAST+ results annotated by category.

### Excel Summary:
Summarizes gene categories, alignment statistics, risk scores, and pathogenicity levels.

### Setup Instructions
1. Set Up BLAST+
Download BLAST+ tools from the NCBI BLAST website.
Unzip the downloaded file and add the BLAST executable directory to your system's PATH.

Test the installation:
bash
Copy code
blastn -version

2. Prepare Input Files
Ensure the FASTA file for query sequences is formatted correctly.
Create a BLAST-compatible reference database using makeblastdb:
bash
Copy code
makeblastdb -in <input_fasta> -dbtype nucl -out reference_db

3. Verify Python Environment
Install Python 3.8 or later.
Install required Python libraries:
bash
Copy code
pip install pandas openpyxl biopython

4. Run the Pipeline
Modify the script to match local file paths.
Execute the script from the terminal:
bash
Copy code
python zoonomix.py --input query_sequences.fasta --dbpath /path/to/databases --output results.csv

## License

ZoonomiX is free to use and share. 

**BLAST+ (Basic Local Alignment Search Tool)**, a core component of this pipeline, is also free to use and distributed under the terms of the **Public Domain Notice** from the National Center for Biotechnology Information (NCBI). For more details, visit the [NCBI BLAST+ License](https://www.ncbi.nlm.nih.gov/IEB/ToolBox/CPP_DOC/lxr/source/doc/publicdomain.txt).

Users are encouraged to comply with any licenses for third-party tools or data used alongside this pipeline.

## Contact

For inquiries, suggestions, or collaborations, please contact me at **research.umeshkumarku@gmail.com** or open an issue in this repository.

