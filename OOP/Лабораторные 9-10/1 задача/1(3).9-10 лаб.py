import json
import os

# Функция для запроса данных у пользователя
def get_user_input():
    user_name = input('Введите ваше имя: ')
    time = input('Сколько лет прошло с последней встречи? ')
    item = input('Какой предмет вы хотите получить? ')
    place = input('Где вы предпочитаете сесть? ')
    return user_name, time, item, place

# Функция для чтения данных из файла JSON
def read_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['user_name'], data['time'], data['item'], data['place']

# Функция для заполнения шаблона данными
def render_template(user_name, time, item, place):
    template = f'Приветствую тебя, {user_name}! Очень рад тебя видеть! С нашей последней встречи прошло {time} лет… Прими этот {item} и садись {place}'
    return template

# Основная логика программы
def main():
    json_file_path = 'data.json'
    
    # Проверяем, существует ли файл JSON с данными
    if os.path.exists(json_file_path):
        user_name, time, item, place = read_data_from_json(json_file_path)
    else:
        user_name, time, item, place = get_user_input()
    
    # Заполняем шаблон данными
    rendered_text = render_template(user_name, time, item, place)
    
    # Выводим результат
    print(rendered_text)

# Точка входа в программу
if __name__ == '__main__':
    main()


# Чтобы использовать эту программу, нужно сохранить код в файл с расширением .py, например, answers_filler.py. 
# Затем необходимо запустить программу в командной строке или терминале. 
# Если файл data.json существует в той же директории, что и программа, она будет использовать данные из этого файла. 
# В противном случае программа запросит данные у пользователя.
# Файл data.json должен быть следующего содержания:
#{
    #'user_name': 'Иван',
   # 'time': '5',
    #'item': 'подарок',
    #'place': 'за столом'
#}