import glob
import pandas as pd

# Get a list of all the csv files in the directory
table_files = glob.glob('table_*.csv')

# Load each csv file into a dataframe
tables = {file_name: pd.read_csv(file_name) for file_name in table_files}

# Print the content of each dataframe
for file_name, table in tables.items():
    print(f"Content of {file_name}:")
    print(table)
    print()
