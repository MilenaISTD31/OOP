import json
from datetime import datetime
import csv

# Функция для запроса данных у пользователя
def get_user_input():
    character1 = input('Введите имя первого персонажа: ')
    character2 = input('Введите имя второго персонажа: ')
    competition = input('Введите вид соревнования: ')
    char1_stats = int(input(f'Введите характеристики {character1} в данном виде деятельности: '))
    char2_stats = int(input(f'Введите характеристики {character2} в данном виде деятельности: '))
    return character1, character2, competition, char1_stats, char2_stats

# Функция для определения победителя и подготовки данных
def determine_winner(character1, character2, competition, char1_stats, char2_stats):
    date_of_competition = datetime.now().strftime('%Y-%m-%d')
    if char1_stats > char2_stats:
        winner = character1
        winner_stats = char1_stats
    elif char2_stats > char1_stats:
        winner = character2
        winner_stats = char2_stats
    else:
        winner = 'Ничья'
        winner_stats = char1_stats # Предполагаем, что характеристики равны
    return winner, winner_stats, competition, date_of_competition

# Функция для вывода данных в формате JSON
def output_json(winner, winner_stats, competition, date_of_competition):
    data = {
        'winner': winner,
        'winner_stats': winner_stats,
        'competition': competition,
        'date_of_competition': date_of_competition
    }
    print(json.dumps(data, ensure_ascii=False, indent=4))

# Функция для вывода данных в формате CSV
def output_csv(winner, winner_stats, competition, date_of_competition):
    with open('competition_result.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['winner', 'winner_stats', 'competition', 'date_of_competition'])
        writer.writerow([winner, winner_stats, competition, date_of_competition])

# Основная логика программы
def main():
    character1, character2, competition, char1_stats, char2_stats = get_user_input()
    winner, winner_stats, competition, date_of_competition = determine_winner(character1, character2, competition, char1_stats, char2_stats)
    
    # Выбор формата вывода
    format_choice = input('Введите формат вывода (json/csv): ').lower()
    if format_choice == 'json':
        output_json(winner, winner_stats, competition, date_of_competition)
    elif format_choice == 'csv':
        output_csv(winner, winner_stats, competition, date_of_competition)
    else:
        print("Неверный формат вывода. Пожалуйста, выберите 'json' или 'csv'.")

def run(self):
        self.output_csv()
        self.output_json()
        result = self.compare_and_render()

        with open('result1.json', 'w') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=4)

        with open('result1.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=result.keys())
            writer.writeheader()
            writer.writerow(result)

if __name__ == '__main__':
    main()