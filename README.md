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

| Database Name                 | Number of Sequences | Description                                   |
|-------------------------------|---------------------|-----------------------------------------------|
| `Adherence_genes.fasta`       | 5,201               | Genes related to microbial adherence.         |
| `Biofilm_genes.fasta`         | 814                 | Biofilm-related genes aiding persistence.     |
| `Efflux_genes.fasta`          | 93                  | Efflux pump genes for multidrug resistance.   |
| `Exotoxin_genes.fasta`        | 1,324               | Genes encoding exotoxins.                    |
| `ICE_genes.fasta`             | 1,326               | Genes linked to Integrative and Conjugative Elements. |
| `Resistance_genes.fasta`      | 3,151               | Known antibiotic resistance genes.           |
| `T3SS_genes.fasta`            | 925                 | Genes for Type 3 Secretion Systems.          |
| `T4SS_genes.fasta`            | 10,795              | Genes for Type 4 Secretion Systems.          |
| `T6SS_genes.fasta`            | 1,411               | Genes for Type 6 Secretion Systems.          |
| `Virulance_genes_Zoonotic.fasta` | 13                 | Zoonotic virulence factors.                  |

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
