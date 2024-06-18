import glob
import pandas as pd

# Get a list of all the csv files in the directory
csv_files = glob.glob('*.csv')

# Read each csv file into a dataframe
dfs = {file_name: pd.read_csv(file_name) for file_name in csv_files}


# Order each dataframe by the first column
dfs = {file_name: dfs[file_name].sort_values(by=dfs[file_name].columns[0]) for file_name in csv_files}


# Create a new csv for each dataframe only containing the columns column_name and data type
for file_name, df in dfs.items():
    new_df = df[['column_name', 'data_type']]
    new_filename = file_name.replace("columns_","")
    new_df.to_csv(f'{file_name}_table.csv', index=False)

