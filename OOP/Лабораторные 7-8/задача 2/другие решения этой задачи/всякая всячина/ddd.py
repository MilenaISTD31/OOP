import csv
import json

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


# Преобразование в CSV
with open('Города.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Индекс", "Тип регион", "Регион", "Город", "Население"])
    for city in "Города":
        writer.writerow([city.index, str(city.type), city.region, city.city_name, city.population])

# Преобразование в JSON
city_data = []
for city in "Города":
    city_data.append({"Индекс": city.index, "Тип региона": city.type, "Регион": city.region, "Город": city.city_name, "Население": city.population})

with open('cities.json', 'w') as jsonfile:
    json.dump(city_data, jsonfile, indent=4)
