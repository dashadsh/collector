import csv
import os

# List of CSV files to compare in the respective folders
csv_files = ['file1.csv', 'file2.csv']

# Folder paths relative to the script location
folder1 = 'old_folder'
folder2 = 'new_folder'

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct full paths to the folders relative to the script location
folder1_path = os.path.join(script_dir, folder1)
folder2_path = os.path.join(script_dir, folder2)

for csv_file in csv_files:
    old_csv_path = os.path.join(folder1_path, csv_file)
    new_csv_path = os.path.join(folder2_path, csv_file)

    # Check if the file is empty
    if os.stat(old_csv_path).st_size == 0:
        print(f'\n-----------------------------------------') 
        print(f'File is EMPTY: {old_csv_path}')
        continue

    if os.stat(new_csv_path).st_size == 0:
        print(f'\n-----------------------------------------') 
        print(f'File is EMPTY: {new_csv_path}')
        continue

    with open(old_csv_path, 'r') as f1, open(new_csv_path, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)

        # Read headers and first rows
        try:
            f1_header = next(reader1)
            f1_row1 = next(reader1)
        except StopIteration:
            print(f'File {old_csv_path} is malformed or has no data.')
            continue

        try:
            f2_header = next(reader2)
            f2_row1 = next(reader2)
        except StopIteration:
            print(f'File {new_csv_path} is malformed or has no data.')
            continue

    print(f'\n-----------------------------------------') 
    if f1_row1 != f2_row1:
        print(f'\nDIFFERENCES FOUND in: {csv_file}\n')
        for index, (old_value, new_value) in enumerate(zip(f1_row1, f2_row1)):
            if old_value != new_value:
                print(f'{f1_header[index]}: Old value: {old_value}, New value: {new_value}')
        print('\n')
    else:
        print(f'No differences found in: {csv_file}')
