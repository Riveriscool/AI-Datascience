import pandas as pd

# Load first Excel file into a DataFrame
file1_path = '/Users/riverwalser/Physics/~$verynewfiel.xlsx'
df1 = pd.read_excel(file1_path)

# Load second Excel file into a DataFrame
file2_path = 'path_to_file2.xlsx'
df2 = pd.read_excel(file2_path)

# Perform left merge
def Merge_datasets(df1, df2):
    
    return new_dataframe

# Export merged DataFrame to a new Excel file
output_file_path = 'path_to_output_file.xlsx'
merged_df.to_excel(output_file_path, index=False)