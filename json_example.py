import json

json_data = '[{"name": "Petr", "age": 20, "is_student": false}]'

parsed_data = json.loads(json_data)

print(f"parsed_data: {parsed_data},\nparsed_data_type: {type(parsed_data)},\ntype_of_[0]: {type(parsed_data[0])}")
print(parsed_data[0]["age"])  # получаем значение ключа в словаре

data = {
    'name': 'Ilya',
    'age': 30,
    'is_student': False
}

json_string = json.dumps(data, indent=2)    # indent - Добвление форматирования
print(json_string)

# Вычитываем JSON
with open('json_example.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

# Записываем в JSON
with open('data.json', mode='w', encoding='utf-8') as file:
    json.dump(data,file, indent=4, ensure_ascii=False)  # ensure_ascii - обработка кириллицы
