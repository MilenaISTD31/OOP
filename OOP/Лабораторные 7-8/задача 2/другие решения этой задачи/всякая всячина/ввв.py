import csv
import json

class City:
    def __init__(self, name, population, region, index):
        self.name = name
        self.population = population
        self.region = region
        self.index = index

    def __hash__(self):
        return hash((self.name, self.region))

    def __eq__(self, other):
        return (self.name, self.region) == (other.name, other.region)

cities = set()

# Чтение данных из CSV файла
with open('Города.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        city = City(row['name'], row['population'], row['region'], row['index'])
        cities.add(city)

# Чтение данных из JSON файла
with open('Города.json', 'r') as file:
    data = json.load(file)
    for city_data in data:
        city = City(city_data['name'], city_data['population'], city_data['region'], city_data['index'])
        cities.add(city)

# Запись уникальных городов в новый CSV файл
with open('unique_cities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'population', 'region', 'index'])
    for city in cities:
        writer.writerow([city.name, city.population, city.region, city.index])

# Запись уникальных городов в новый JSON файл
unique_cities_list = []
for city in cities:
    unique_cities_list.append({'name': city.name, 'population': city.population, 'region': city.region, 'index': city.index})

with open('unique_cities.json', 'w') as file:
    json.dump(unique_cities_list, file, indent=4)