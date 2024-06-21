import hashlib
from pathlib import Path
from pprint import pprint

load = 1
path = Path.home() / "Downloads"
FILE_HASHCODE = {}


def hash_code(path):
    hash_data = hashlib.sha256()
    with open(path, 'rb') as f:
        for octet in iter(lambda: f.read(4096), b""):
            hash_data.update(octet)
    FILE_HASHCODE[path.name] = hash_data.hexdigest()
    return FILE_HASHCODE


def get_all_file():
    # Touver pourquoi le résultat retourne WindowsPath et pas juste le chemin
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
