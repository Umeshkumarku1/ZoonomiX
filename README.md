# ZoonomiX 🚀  

## A Bioinformatics Pipeline for Microbial Genomic Analysis and Risk Prediction  

## 🔬 Introduction  

ZoonomiX is an **advanced bioinformatics pipeline** designed to **analyze microbial genomes**, **identify critical genes**, and **predict their roles** in:  

- **Antibiotic resistance**  
- **Virulence**  
- **Pathogenicity**  
- **Zoonotic potential**  

By leveraging **BLASTn** and **curated reference databases**, ZoonomiX systematically evaluates **microbial adaptability and future risks**.  

Understanding the **genetic makeup of microbes** is essential in combating:  

- **Antimicrobial resistance (AMR)**  
- **Zoonotic diseases**  
- **Emerging infectious threats**  

ZoonomiX provides a **user-friendly, customizable, and efficient** solution for researchers studying:  

- **Microbial evolution**  
- **Host-pathogen interactions**  
- **Horizontal gene transfer (HGT)**
  
## 🔑 Key Features  

✅ **Gene Identification**  

- Detects genes linked to **adherence, biofilm formation, efflux pumps, virulence factors, and more**.  
- Supports **custom and curated reference databases** for enhanced accuracy.  

✅ **Resistance and Pathogenicity Prediction**  

- Identifies genes contributing to **antibiotic resistance** and **virulence**.  
- Scores microbes based on their **pathogenicity and zoonotic risk**.  

✅ **Comprehensive Analysis with Curated Databases**  

ZoonomiX integrates **genetic markers** such as:  

- **Adherence factors**  
- **Biofilm-related genes**  
- **Efflux pumps**  
- **Exotoxins**  
- **Integrative and Conjugative Elements (ICEs)**  
- **Secretion Systems (T3SS, T4SS, T6SS)**  
- **Zoonotic virulence factors**  

✅ **Customizable Parameters**  

- User-defined thresholds for **BLASTn alignment**:  
  - **E-value**  
  - **Percent identity**  
  - **Query coverage**  

✅ **Detailed Outputs**  

- **Tabular reports** with **gene annotations, alignment statistics, and risk scores**.  
- **Summarized Excel files** for easy interpretation.  
---

## 📂 Reference Databases  

ZoonomiX relies on curated **FASTA** reference databases:  

| **Database Name**             | **Number of Sequences** | **Description**                                      |
|------------------------------|------------------------|------------------------------------------------------|
| **Adherence_genes**          | 5,201                  | Genes related to microbial adherence.               |
| **Biofilm_genes**            | 814                    | Biofilm-related genes aiding persistence.           |
| **Efflux_genes**             | 93                     | Efflux pump genes for multidrug resistance.         |
| **Exotoxin_genes**           | 1,324                  | Genes encoding exotoxins.                           |
| **ICE_genes**                | 1,326                  | Genes linked to Integrative & Conjugative Elements. |
| **Resistance_genes**         | 3,151                  | Known antibiotic resistance genes.                  |
| **T3SS_genes**               | 925                    | Genes for Type 3 Secretion Systems.                 |
| **T4SS_genes**               | 10,795                 | Genes for Type 4 Secretion Systems.                 |
| **T6SS_genes**               | 1,411                  | Genes for Type 6 Secretion Systems.                 |
| **Virulence_genes_Zoonotic**  | 13                     | Zoonotic virulence factors.                         |


# ⚙️ Prerequisites  

### 1️⃣ Hardware Requirements  
- A **computer with sufficient RAM and storage** for bioinformatics tasks.  
- **Stable internet connection** to download tools and databases.  

### 2️⃣ Software Requirements  

#### **Python Environment**  
- **Python 3.8 or later**  
- Install required Python libraries:  
  ```bash
  pip install pandas openpyxl biopython

### 🧬 BLAST+ (Basic Local Alignment Search Tool)  

1. **Download and Install BLAST+**  
   - Get BLAST+ from the **[NCBI BLAST website](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)**.  
   - Extract the downloaded files and install them on your system.  

2. **Add BLAST executables to system PATH**  
   - Ensure the BLAST+ executables (`blastn`, `makeblastdb`) are accessible from the command line.  
   - On Linux/macOS, add the BLAST directory to your `.bashrc` or `.zshrc` file:  
     ```bash
     export PATH=$PATH:/path/to/blast/bin
     ```
   - On Windows, add the BLAST+ installation path to **System Environment Variables**.

3. **Test Installation**  
   - Open a terminal and check the version:  
     ```bash
     blastn -version
     ```

---

### 📊 Spreadsheet Software  
- **Microsoft Excel**, **LibreOffice**, or **Google Sheets** to view output files.  

### 📝 Text Editor/IDE  
- Recommended editors:  
  - **VSCode**  
  - **PyCharm**  
  - **Any plain text editor**  


## 🔧 Setup Instructions  

### 1️⃣ Set Up BLAST+  
1. **Download BLAST+** from the **[NCBI BLAST website](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)**.  
2. **Unzip the downloaded file** and place it in an accessible directory.  
3. **Add BLAST+ executables** (e.g., `blastn`, `makeblastdb`) to your system's PATH.  
4. **Test the installation** by running:  
   ```bash
   blastn -version
   
## 🔧 Setup Instructions  

### 1️⃣ Set Up BLAST+  
1. **Download BLAST+** from the **[NCBI BLAST website](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)**.  
2. **Unzip the downloaded file** and place it in an accessible directory.  
3. **Add BLAST+ executables** (e.g., `blastn`, `makeblastdb`) to your system's PATH.  
4. **Test the installation** by running:  
   ```bash
   blastn -version
   
2️⃣ Prepare Input Files

Ensure the FASTA file for query sequences is formatted correctly.
Create a BLAST-compatible reference database:
bash
Copy
Edit
makeblastdb -in <input_fasta> -dbtype nucl -out reference_db
Use the provided prebuilt reference database:
Download reference_db.nsq

3️⃣ Verify Python Environment
Install Python 3.8+ and required dependencies:
bash
Copy
Edit
pip install pandas openpyxl biopython

▶️ Running ZoonomiX
Modify the script to match your local file paths, then execute:

bash
Copy
Edit
python zoonomix.py --input query_sequences.fasta --dbpath /path/to/databases --output results.csv


## 📜 License  

ZoonomiX is **free to use and share**.  

**BLAST+ (Basic Local Alignment Search Tool)** is distributed under the **Public Domain Notice** from the **National Center for Biotechnology Information (NCBI)**.  

Users should comply with any **licenses for third-party tools or datasets** used alongside this pipeline.  

---

## 🤝 Contribute  

👨‍💻 **Contributions are welcome!** If you'd like to:  
- **Report issues**  
- **Suggest new features**  
- **Submit a pull request**  

Feel free to **open an issue** in this repository.  

---

## 📩 Contact  

For inquiries, suggestions, or collaborations, reach out at:  
📧 **Email:** [research.umeshkumarku@gmail.com](mailto:research.umeshkumarku@gmail.com)  

---

## 📌 Citation  

If you use **ZoonomiX** in your research, please **cite it appropriately**!  

---

## 🚀 Get Started with ZoonomiX and Unlock Insights into Microbial Genomics!  

🔗 **GitHub Repository Link:** *(https://github.com/Umeshkumarku1/ZoonomiX)*  
