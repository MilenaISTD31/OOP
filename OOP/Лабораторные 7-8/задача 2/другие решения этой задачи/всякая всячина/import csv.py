import csv
import json
# Эти строки импортируют модули csv и json, которые позволяют работать с файлами в форматах CSV и JSON соответственно

class City: # Здесь мы объявляем класс City, который будет использоваться для представления городов и их данных
    def __init__(self, index, type, region, city_name, population): # Это конструктор класса City. Он инициализирует экземпляр класса с именем, населением, регионом и индексом.
        self.type = type
        self.population = population
        self.region = region
        self.index = index
        self.city_name = city_name

    def __hash__(self): # Метод __hash__ возвращает хеш-значение объекта. В данном случае хеш вычисляется на основе имени, региона и индекса города
        # Метод __hash__ определяет хеш-значение для объекта. В Python хеш-значения используются, например, когда объекты добавляются в множество (set). Здесь хеш вычисляется на основе кортежа, содержащего имя, регион и индекс города.
        return hash((self.index, self.type, self.region, self.city_name, self.population))

    def __eq__(self, other): # Метод __eq__ определяет, равен ли один объект City другому, сравнивая их имя, регион и индекс
        # Метод __eq__ используется для сравнения двух объектов класса City. Если имя, регион и индекс одного объекта совпадают с таковыми у другого объекта, то они считаются равными.
        return (self.index, self.type, self.region, self.city_name, self.population) == (other.index, other.type, other.region, other.city_name, other.population)

def read_csv(file_path): # Функция read_csv читает данные из файла CSV и возвращает список экземпляров City.
    # В этом блоке кода файл открывается в режиме чтения ('r') с указанием кодировки 'utf-8'. csv.DictReader создает объект, который читает строки из файла и преобразует их в словари, где ключи — это заголовки столбцов, а значения — данные из соответствующих ячеек. Для каждой строки создается новый объект City, который затем добавляется в список.
    with open(file_path, mode='r', encoding='utf-8') as f: # Этот блок открывает файл CSV, читает его содержимое и создает список объектов City на основе данных в файле
        reader = csv.DictReader(f)
        return [City(row['Индекс'], row['Тип региона'], row['Регион'], row['Город'], row['Население']) for row in reader]

def read_json(file_path): # Функция read_json выполняет ту же функцию, что и read_csv, но для файлов JSON
    # Этот блок открывает файл JSON, читает его содержимое и создает список объектов City.
    with open(file_path, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        return [City(item['Индекс'], item['Тип региона'], item['Регион'], item['Город'], item['Население']) for item in data]

def save_to_csv(cities, file_path): # Функция save_to_csv сохраняет список городов в файл CSV
   # Этот блок открывает файл для записи и сохраняет в него данные о городах
   # В этом блоке файл открывается для записи ('w'). Создается объект writer, который используется для записи строк в файл. Сначала записывается строка с заголовками, а затем — данные каждого города.
    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Индекс", "Тип региона", "Регион", "Город", "Население"])
        for city in cities:
            writer.writerow([city.index, city.type, city.region, city.city_name, city.population])

def save_to_json(cities, file_path): # Функция save_to_json сохраняет список городов в файл JSON.
    # Этот блок открывает файл для записи и сохраняет в него данные о городах в формате JSON
    with open(file_path, mode='w', encoding='utf-8') as f:
        json.dump([city.__dict__ for city in cities], f, ensure_ascii=False, indent=4)

# Предположим, что пути к файлам следующие:
csv_file_path = 'Города.csv'
json_file_path = 'Города.json'

# Чтение данных
cities_csv = read_csv(csv_file_path)
cities_json = read_json(json_file_path)

# Объединение уникальных городов
unique_cities = list(set(cities_csv + cities_json))

# Сохранение новых списков
save_to_csv(unique_cities, 'unique_cities.csv')
save_to_json(unique_cities, 'unique_cities.json')