from pathlib import Path
# Set path
file = Path.cwd() / 'info.txt'
# Create new file for result
new_file = Path.cwd() / 'Name.txt'
new_file.touch()
# open info.txt
with open(file, "r") as f:
    content_info_txt = f.read().splitlines()
#create a list with info.txt
name = []
for lines in content_info_txt:
    name.extend(lines.split())
# Clean list
cleaner = [n.strip(",") for n in name]
print(cleaner)
# .join and sort the list to write in the new file.
with open(new_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(sorted(cleaner)))
