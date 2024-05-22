import csv # module or reading and writing CSV (Comma-Separated Values) files.
import os # provides a way to use operating system dependent functionality like reading & writing to the file system.


# List of CSV files to compare in the respective folders
csv_files = ['file1.csv', 'file2.csv']

# Folder paths relative to the script location
folder1 = 'old_folder'
folder2 = 'new_folder'

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__)) # represents the path to the Python script (or module) currently being executed.

# Construct full paths to the folders relative to the script location
folder1_path = os.path.join(script_dir, folder1)
folder2_path = os.path.join(script_dir, folder2)

for csv_file in csv_files:
    old_csv_path = os.path.join(folder1_path, csv_file)
    new_csv_path = os.path.join(folder2_path, csv_file)

    # Check if the file is empty
	# os.stat() function from the os module to get information about the specified file (new_csv_path). 
	# returns a stat_result object containing various pieces of information about the file, 
	# such as its size, permissions, and timestamps.
	#
	# .st_size: accesses the st_size attribute of the stat_result object, 
	# which represents the size of the file in bytes.
    if os.stat(old_csv_path).st_size == 0:
        print(f'\n-----------------------------------------') 
        print(f'File is EMPTY: {old_csv_path}')
        continue

    if os.stat(new_csv_path).st_size == 0:
        print(f'\n-----------------------------------------') 
        print(f'File is EMPTY: {new_csv_path}')
        continue

    with open(old_csv_path, 'r') as f1, open(new_csv_path, 'r') as f2:
		# csv.reader(): function from csv module. It takes a file-like object 
		# (such as an open file or a file-like object returned by io.StringIO) as its argument 
		# and returns a CSV reader object.
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)

        # Read headers and first rows
        try:
			# next - built-in Python function that is used to retrieve the next item from an iterator
            f1_header = next(reader1)
            f1_row1 = next(reader1)
		# StopIteration - built-in exception in Python that is raised when an iterator has no further items to yield. 
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
