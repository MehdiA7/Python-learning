import hashlib
from pathlib import Path
from pprint import pprint
# Declare variables
load = 1
path = Path.home() / "Downloads"
FILE_HASHCODE = {}


def hash_code(file_path):
    """
Calculate the hash code of a file.

Args:
    file_path (str): The path to the file for which to calculate the hash code.

Returns:
    dict: A dictionary containing the file name as key and its hash code as value.
"""

    # Create a variable for hash code file
    hash_data = hashlib.sha256()
    # Open the file in binary
    with open(file_path, 'rb') as f:
        # Read the file in blocks of 4096 bytes until it returns an empty string
        for octet in iter(lambda: f.read(4096), b""):
            # Put all in hash_data
            hash_data.update(octet)
    # Put the result in dictionary with file Name and return
    FILE_HASHCODE[file_path.name] = hash_data.hexdigest()
    return FILE_HASHCODE


def get_all_file():
    """
    Get all files in the specified path.

    Returns:
        list: A list of Path objects representing files in the specified path.
    """
    return [f for f in path.glob('*') if f.is_file()]
    # return list(path.rglob('*'))


all_path = get_all_file()


for way in all_path:
    print(f"File Analysis : {load}")
    load += 1
    hash_code(way)

# Create a dictionary return to detect duplicates files
DUPLICATE_FILE = {}
for file_name, code in FILE_HASHCODE.items():
    DUPLICATE_FILE.setdefault(code, set()).add(file_name)

result = [key for key, values in DUPLICATE_FILE.items() if len(values) > 1]
print("\nHere are the files that are duplicates in your folders :\n")

for name in result:
    result_list = list(DUPLICATE_FILE[name])
    for file in result_list:
        print(file)
    print(75*'-')