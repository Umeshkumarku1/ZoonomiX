# ZoonomiX Pipeline

ZoonomiX is a bioinformatics pipeline designed to analyze microbial genomes, predict resistance and virulence traits, and assess zoonotic potential. The pipeline uses **BLASTn** to compare nucleotide sequences against specialized reference databases and generates a comprehensive tabular report for detailed analysis.

## Features

- **Comprehensive Gene Analysis**:
  - Identifies genes related to adherence, biofilm formation, efflux pumps, secretion systems, virulence, resistance, and more.
- **Database Integration**:
  - Utilizes curated FASTA reference databases for critical gene categories.
- **Scoring and Risk Prediction**:
  - Quantifies risks for pathogenicity, resistance, and zoonotic transmission.
- **Customizable Parameters**:
  - Offers user-defined thresholds for BLASTn alignment (e.g., E-value, identity, coverage).

## Reference Databases

ZoonomiX leverages the following curated reference databases:

| Database Name                 | Number of Sequences | Description                                   |
|-------------------------------|---------------------|-----------------------------------------------|
| `Adherence_genes.fasta`       | 5,201               | Genes related to microbial adherence to host cells. |
| `Biofilm_genes.fasta`         | 814                 | Genes involved in biofilm formation and persistence. |
| `Efflux_genes.fasta`          | 93                  | Genes coding for efflux pumps, crucial for drug resistance. |
| `Exotoxin_genes.fasta`        | 1,324               | Genes encoding exotoxins that enhance virulence. |
| `ICE_genes.fasta`             | 1,326               | Integrative and Conjugative Elements (ICEs) responsible for horizontal gene transfer. |
| `Resistance_genes.fasta`      | 3,151               | Antibiotic resistance genes.                  |
| `T3SS_genes.fasta`            | 925                 | Genes related to Type 3 Secretion Systems.    |
| `T4SS_genes.fasta`            | 10,795              | Genes associated with Type 4 Secretion Systems. |
| `T6SS_genes.fasta`            | 1,411               | Genes linked to Type 6 Secretion Systems.     |
| `Virulance_genes_Zoonotic.fasta` | 13                 | Zoonotic virulence genes.                     |

## How It Works

1. **Input**: Upload a microbial genome or nucleotide sequence in FASTA format.
2. **BLASTn Analysis**: Compare input sequences against the reference databases.
3. **Data Processing**:
   - Extract BLASTn alignment results (e.g., E-value, identity, coverage).
   - Annotate genes with functional descriptions.
4. **Scoring**:
   - Assign risk scores for pathogenicity, resistance, and zoonotic potential.
5. **Output**:
   - Generate a tabular report for easy visualization and interpretation.

## Installation

## Prerequisites

### 1. Hardware Requirements
- A computer with sufficient **RAM** and **storage** for bioinformatics tasks.
- A stable **internet connection** to download required tools and databases.

### 2. Software Requirements

#### Python Environment
- **Python 3.8 or later.**
- Required Python Libraries:
  - `pandas`: For data manipulation and analysis.
  - `openpyxl`: For working with Excel files.
  - `biopython`: For handling biological sequence data.
- Install the libraries via pip:
  ```bash
  pip install pandas openpyxl biopython


### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ZoonomiX.git
   cd ZoonomiX
