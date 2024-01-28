import pandas as pd

# Load first Excel file into a DataFrame
file1_path = '/Users/riverwalser/Physics/verynewfiel.xlsx'
df1 = pd.read_excel(file1_path)

# Load second Excel file into a DataFrame
file2_path = '/Users/riverwalser/Physics/AMZN (4).xlsx'
df2 = pd.read_excel(file2_path)

print("df1 columns:", df1.columns)
print("df2 columns:", df2.columns)

df3 = df1.merge(df2,how = 'left',left_on='Date',right_on ='Date')

print(df3.describe())
"""# Perform left merge
def mergeDataframes(df1, df2):
    
    merged_dataframe = 
    return merged_dataframe
merged_df = mergeDataframes(df1, df2)
# Export merged DataFrame to a new Excel file"""
output_file_path = 'finalxcelfile.xlsx'
df3.to_excel(output_file_path, index=False)