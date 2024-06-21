import json
from pathlib import Path

current_file_path = Path(__file__)
try_json = current_file_path.parent / "test_result.json"
with open(try_json, "r") as file:
    data = json.load(file)

print(data)
json_string = '{"name": "John", "age": 30, "city": "New York"'
try:
    data = json.loads(json_string)
    print(data)
except json.decoder.JSONDecodeError as e:
    print("Error json proccessing:", e)

data = {
    "name": "Alex",
    "age": 23,
    "city": "Chernigiv",
    "car": {"name": "Zhaporozhec", "year": 1886}
    }

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("***")
