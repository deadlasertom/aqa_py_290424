from pathlib import Path

print(__file__)
print(type(__file__))
current_file_path = Path(__file__)
print(current_file_path)
print(type(current_file_path))
print(current_file_path.parts)
print(current_file_path.parent)
print(current_file_path.parent.parent)
project_path = current_file_path.parent.parent
work_with_csv = project_path / "ideas_for_test" / "work_with_csv"
print(work_with_csv)

print(current_file_path.parents[0])
print(current_file_path.parents[1])
print(current_file_path.parents[3])
print(current_file_path.parents[4])
print(current_file_path.parents[-1])

file_for_test = current_file_path.parent / "file.txt"
print(current_file_path.parent.suffixes) # "dou.com.ua" > .suffixes > ['.com', '.ua']
print(file_for_test.suffix) # .txt
print(file_for_test.stem)  # file
print(file_for_test.name)  # file.txt

# current work dir
print(Path.cwd())
print(Path.home())  # user home

print(file_for_test.exists())
print(file_for_test.parent.exists())

print(current_file_path.is_dir())
print(current_file_path.is_file())
print(file_for_test.is_dir(), file_for_test.is_file())

print([x for x in current_file_path.parent.iterdir()])     # full
print([x for x in current_file_path.parent.glob('*.py')])  # ext only

new_dir = current_file_path.parent / "subfolder" / "sub.sub.folder"
new_dir.mkdir(mode=0o777, parents=True, exist_ok=True)


# with current_file_path.open("r", encoding="utf-8") as file:
#     f = file.read()
# print(f)

with file_for_test.open("r", encoding="utf-8") as file:  # "r+"
    f = file.read()
print(f)
f = f.replace("віконечко", "сонечко")
print(f)
with file_for_test.open("w", encoding="utf-8") as file: # "w+"
    file.write(f)
with file_for_test.open("a", encoding="utf-8") as file: # "a+"
    file.write("\nМені так любо любо стало")


