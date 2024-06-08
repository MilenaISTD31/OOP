import csv
import json

class City:
    def __init__(self, index, region_type, region, city, population):
        self.index = index
        self.region_type = region_type
        self.region = region
        self.city = city
        self.population = population

    def __eq__(self, other):
        if isinstance(other, City):
            return self.city == other.city

    def __hash__(self):
        return hash(self.city)
    
    # def __repr__(self):
    #     return f'\n{self.index} {self.region_type} {self.region} {self.city} {self.population}'

# Функция для чтения данных из CSV файла
def read_csv_file(filename):
    csv_cities = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = City((row['Индекс']), row['Тип региона'], row['Регион'], row['Город'], (row['Население']))
            csv_cities.append(city)
    return csv_cities

# Функция для чтения данных из JSON файла
def read_json_file(filename):
    json_cities = []
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data['data']:
            city = City(item['Индекс'], item['Тип региона'], item['Регион'], item['Город'], item['Население'])
            json_cities.append(city)
    return json_cities

# Функция для записи данных в CSV файл
def write_csv_file(filename, unique_cities):
    with open(filename,'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Индекс', 'Тип региона', 'Регион', 'Город', 'Население'])
        for city in unique_cities:
            writer.writerow([city.index, city.region_type, city.region, city.city, city.population])
    print(f'Файл {filename} готов')

# Функция для записи данных в JSON файл
def write_json_file(filename, unique_cities):
    data = [{'Индекс': city.index, 'Тип региона': city.region_type, 'Регион': city.region, 'Город': city.city, 'Население': city.population} for city in unique_cities]
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)
    print(f'Файл {filename} готов')

file_csv = read_csv_file('Города.csv')    # Сюда помещаем данные из CSV файла
file_json = read_json_file('Города.json')    # А сюда данные из JSON файла

file_union = file_csv + file_json    # Объединяем данные из обоих источников
unique_cities = list(set(file_union))    # Преобразуем коллекцию в список уникальных городов

# Сохраняем уникальные города в CSV и JSON файлы
write_json_file('Уникальные города.json', unique_cities)
write_csv_file('Уникальные города.csv', unique_cities)
