import json
import csv

class CompetitionManager: # Определение класса CompetitionManager, который будет управлять соревнованием между персонажами.
    def __init__(self): # Конструктор класса, который инициализирует словарь characters для хранения информации о персонажах.
        self.characters = {}

    def gather_competition_info(self): # Метод gather_competition_info собирает информацию о персонажах и типе соревнования.
        self.characters['character1'] = {} # Создание словаря для первого персонажа и запрос у пользователя его имени и характеристик.
        self.characters['character1']['name'] = input('Введите имя первого персонажа: ')
        self.characters['character1']['characteristics'] = input('Введите характеристику (в виде числа) первого персонажа в соревновании: ')
        # Аналогично для второго персонажа:
        self.characters['character2'] = {}
        self.characters['character2']['name'] = input('Введите имя второго персонажа: ')
        self.characters['character2']['characteristics'] = input('Введите характеристику (в виде числа) второго персонажа в соревновании: ')
        # Запрос у пользователя типа соревнования:
        self.competition_type = input('Введите вид соревнования: ')
        

    def compare_and_render(self): # Метод compare_and_render сравнивает характеристики персонажей и определяет победителя.
        # Если характеристики первого персонажа больше, он объявляется победителем.
        if self.characters['character1']['characteristics'] > self.characters['character2']['characteristics']:
            winner_name = self.characters['character1']['name']
            winner_characteristics = self.characters['character1']['characteristics']
        # Если характеристики второго персонажа больше, он объявляется победителем.
        elif self.characters['character2']['characteristics'] > self.characters['character1']['characteristics']:
            winner_name = self.characters['character2']['name']
            winner_characteristics = self.characters['character2']['characteristics']
        # Если характеристики равны, объявляется ничья:
        else:
            winner_name = 'Ничья'
            winner_characteristics = 'Характеристики равны'
        # Создание словаря с информацией о победителе и типе соревнования:
        filled_template = {
            'winner_name': winner_name,
            'competition': self.competition_type,
            'winner_characteristics': winner_characteristics,
        }

        return filled_template # Возвращение словаря с результатами соревнования.

    def run(self): # Метод run запускает процесс сбора информации и определения победителя.
        self.gather_competition_info() # Сбор информации о персонажах и соревновании.
        result = self.compare_and_render() # Сравнение персонажей и определение победителя.

        with open('result.json', 'w') as json_file: # Сохранение результатов соревнования в файл result.json.
            json.dump(result, json_file, ensure_ascii=False, indent=4)

        with open('result.csv', 'w', newline='') as csv_file: # Сохранение результатов соревнования в файл result.csv.
            writer = csv.DictWriter(csv_file, fieldnames=result.keys())
            writer.writeheader()
            writer.writerow(result)

if __name__ == '__main__': # Этот блок кода запускает весь процесс, если скрипт выполняется как основная программа.
    competition_manager = CompetitionManager()
    competition_manager.run()