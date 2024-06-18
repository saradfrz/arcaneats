import os
import re

# Directory where the files are located
directory = os.getcwd()

# Pattern to match the filenames
pattern = re.compile(r'^(.+)_table\.csv$')

# Iterate over each file in the directory
for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        value = match.group(1)
        new_filename = f"table_{value}.csv"
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed '{filename}' to '{new_filename}'")

