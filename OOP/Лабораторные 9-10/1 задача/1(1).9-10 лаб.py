import json

# Запрашиваем данные у пользователя
user_name = input('Введите ваше имя: ')
user_time = input('Сколько лет прошло с последней встречи: ')
user_item = input('Введите предмет, который вы получаете: ')
user_place = input('Введите место, где вы можете сесть: ')

# Заполняем шаблон данными
text = f'Приветствую тебя, {user_name}! Очень рад тебя видеть! С нашей последней встречи прошло {user_time} лет... Прими этот {user_item} и садись {user_place}'

# Выводим отрендеренный текст в консоль
print(text)

# Создаем файл с данными
with open('template.txt', 'w') as file:
    file.write(text)

# Создаем файл с ответами в формате JSON
answers = {
    'user_name': user_name,
    'time': user_time,
    'item': user_item,
    'place': user_place
}

with open('answers.json', 'w') as json_file:
    json.dump(answers, json_file)