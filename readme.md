# Investment Excel File Merger

A simple script to merge multiple Excel files (with identical sheet names) from the current directory into a single output file.

## 🔧 Requirements

- Python 3
- `pandas` and `openpyxl` libraries

## 📁 How to Use

1. Place all your `.xlsx` Excel files in one folder.
2. Open a terminal and **navigate to that folder**:
```bash
cd /path/to/your/excel-files-folder
```

3. Run this one-liner command:
```
pip install pandas openpyxl && curl -sL https://raw.githubusercontent.com/avinashknagar/investment-file-merger/main/merger.py -o merger.py && python3 merger.py
```

4. A file named merged_output.xlsx will be created in the same folder.