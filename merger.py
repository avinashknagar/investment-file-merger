import pandas as pd
import os

def get_excel_files_from_directory(directory="."):
    return [f for f in os.listdir(directory) if f.endswith((".xlsx", ".xls"))]

def merge_excel_files(files):
    if not files:
        print("No Excel files found in the current directory.")
        return {}

    # Load sheet names from the first file
    sheet_names = pd.ExcelFile(files[0]).sheet_names
    merged_data = {sheet: [] for sheet in sheet_names}

    for file in files:
        print(f"Processing: {file}")
        xls = pd.ExcelFile(file)
        for sheet in sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet, header=1)
            merged_data[sheet].append(df)

    # Concatenate each sheet
    for sheet in sheet_names:
        merged_data[sheet] = pd.concat(merged_data[sheet], ignore_index=True)

    return merged_data

def save_merged_excel(merged_data, output_file):
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for sheet, df in merged_data.items():
            df.to_excel(writer, sheet_name=sheet, index=False)

    print(f"\nMerged file saved as: {output_file}")

# === Main script ===
if __name__ == "__main__":
    current_directory = os.getcwd()
    excel_files = get_excel_files_from_directory(current_directory)
    print("Found Excel files:", excel_files)

    merged_sheets = merge_excel_files(excel_files)

    if merged_sheets:
        output_file = "merged_output.xlsx"
        save_merged_excel(merged_sheets, output_file)
