import csv
import json
from jinja2 import Template # Эта строка импортирует класс Template из библиотеки jinja2, который используется для рендеринга шаблонов.


class City:
    def __init__(self, path_csv=None, path_json=None): # Это конструктор класса, который инициализирует новый объект City. 
        #Он принимает два необязательных параметра: пути к файлам CSV и JSON.
        self.cities = set() # Создаётся пустое множество cities, которое будет использоваться для хранения уникальных данных о городах.
        self.path_csv = path_csv # Эти строки сохраняют пути к файлам CSV и JSON в атрибутах объекта.
        self.path_json = path_json 
        if path_csv: # Если были предоставлены пути к файлам, вызываются методы read_csv и read_json для чтения данных.
            self.read_csv(path_csv)
        if path_json:
            self.read_json(path_json)

    def to_dict(self, name, population, region, index): # Метод to_dict принимает данные о городе и возвращает их в виде словаря.
        return { # Создаётся и возвращается словарь с данными о городе.
            "name": name,
            "population": population,
            "region": region,
            "index": index
        }

    def read_csv(self, file_path): # Метод read_csv принимает путь к файлу CSV и читает его содержимое.
        with open(file_path, mode='r', encoding='utf-8') as file: # Открывается файл CSV для чтения с указанием кодировки UTF-8.
            reader = csv.DictReader(file) # Создаётся объект DictReader, который преобразует каждую строку файла CSV в словарь.
            for row in reader: # Итерация по строкам файла CSV.
                city = self.to_dict(row['Город'], row['Население'], row['Регион'], row['Индекс']) # Для каждой строки создаётся словарь с данными о городе, используя метод to_dict.
                self.cities.add(tuple(city.items())) # Преобразованный словарь в кортеж добавляется в множество cities, чтобы избежать дублирования.

    def read_json(self, file_path): # Метод read_json аналогичен read_csv, но для файлов JSON.
        with open(file_path, mode='r', encoding='utf-8') as file: # Открывается файл JSON для чтения.
            data = json.load(file) # Содержимое файла JSON загружается в переменную data.
            for item in data['data']: # Итерация по элементам, содержащимся в ключе data загруженного JSON.
                city = self.to_dict(item['Город'], item['Население'], item['Регион'], item['Индекс']) # Для каждого элемента создаётся словарь с данными о городе.
                self.cities.add(tuple(city.items())) # Данные о городе добавляются в множество cities.

    def get_cities_list(self): # Метод get_cities_list возвращает список словарей с данными о городах.
        return [dict(city) for city in self.cities] # Преобразует каждый кортеж обратно в словарь и возвращает список словарей

# Чтение данных из файлов
path_csv = 'Города.csv'
path_json = 'Города.json'

city_handler = City(path_csv, path_json)
cities_list = city_handler.get_cities_list()

# HTML шаблон
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список городов</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #FFFFE0;
        }
    </style>
</head>
<body>
    <h1>Список городов</h1>
    <table>
        <thead>
            <tr>
                <th>Город</th>
                <th>Население</th>
                <th>Регион</th>
                <th>Индекс</th>
            </tr>
        </thead>
        <tbody>
            {% for city in cities %}
            <tr>
                <td>{{ city.name }}</td>
                <td>{{ city.population }}</td>
                <td>{{ city.region }}</td>
                <td>{{ city.index }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

# Рендеринг HTML с данными
template = Template(html_template)
rendered_html = template.render(cities=cities_list)

# Сохранение результата в файл result.html
with open('result.html', mode='w', encoding='utf-8') as file:
    file.write(rendered_html)
