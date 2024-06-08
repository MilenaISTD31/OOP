import csv
import json

class City:
    def __init__(self, index, region_type, region, name, population):
        self.index = index
        self.region_type = region_type
        self.region = region
        self.name = name
        self.population = population

    def __hash__(self):
        return hash((self.index, self.region_type, self.region, self.name))

    def __eq__(self, other):
        return isinstance(other, City) and (self.index, self.region_type, self.region, self.name) == (other.index, other.region_type, other.region, other.name)

cities = set()

# Считывание данных из csv
with open('Города.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        city = City(row['Индекс'], row['Тип региона'], row['Регион'], row['Город'], row['Население'])
        cities.add(city)

# Преобразование множества городов в список
city_list = list(cities)

# Сохранение в формат CSV
with open('cities_unique.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Индекс', 'Тип региона', 'Регион', 'Город', 'Население'])
    for city in city_list:
        writer.writerow([city.index, city.region_type, city.region, city.name, city.population])

# Сохранение в формат JSON
city_json = [{'Индекс': city.index, 'Тип региона': city.region_type, 'Регион': city.region, 'Город': city.name, 'Население': city.population} for city in city_list]
with open('cities_unique.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(city_json, jsonfile, ensure_ascii=False, indent=4)

# Функция для поиска города
def search_city(city_name):
    for city in city_list:
        if city.name.lower() == city_name.lower():
            return city
    return None

# Ваш запрос на поиск города
city_name = input("Введите название города для поиска: ")
found_city = search_city(city_name)

if found_city:
    print(f"Город \"{found_city.name}\" найден:")
    print(f"Индекс: {found_city.index}")
    print(f"Тип региона: {found_city.region_type}")
    print(f"Регион: {found_city.region}")
    print(f"Население: {found_city.population}")
else:
    print(f"Город \"{city_name}\" не найден.")

print("Данные успешно обработаны и сохранены.")
