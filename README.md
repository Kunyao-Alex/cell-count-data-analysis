# Cell Count Data Analysis Project

## Overview
This project conducts analysis on cell count data: calculating the relative frequencies of immune cell populations, generating comparative boxplots for responders vs. non-responders, and performing statistical analysis using t-tests.

## Prerequisites
Ensure you have the following installed on your Unix-based system:
- Python 3.8+
- pip (Python package manager)

### Install Required Packages
```bash
pip install pandas seaborn matplotlib scipy
```

## Input and Output Files
- `cell-count.csv`: Input data containing cell count information.
- `relative_frequencies.csv`: Output CSV with calculated relative frequencies.
- `boxplots.png`: Visualization of responders vs. non-responders.

## How to Run
1. Navigate to the project directory using the terminal.
```bash
cd /path/to/project
```

2. Run the Python script.
```bash
python cell_count_analysis.py
```

3. Check the terminal output and output files in the same directory.

## Troubleshooting
- Ensure the CSV file `cell-count.csv` is present in the same directory.
- Verify the Python version and the required packages are installed.
- If `pip install pandas seaborn matplotlib scipy` or `python cell_count_analysis.py` doesn't work, try using `pip3` and `python3` instead:
```bash
pip3 install pandas seaborn matplotlib scipy
python3 cell_count_analysis.py
```