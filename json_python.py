import json

data_of_Maria = {
    'name': 'Мария',
    'age': 25,
    'is_student': True
}

with (open("json_example.json", "r", encoding="utf-8") as file):
    read_data = json.load(file)
    print(read_data)

with open("json_user.json", "w", encoding='utf-8') as file:
    json.dump(data_of_Maria, file, indent=4, ensure_ascii=False)