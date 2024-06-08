import json
from jinja2 import Environment, FileSystemLoader

# Функция для заполнения шаблона данными и вывода результата
def render_template(template_data):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template('templates.txt')
    output = template.render(template_data)
    print(output)

# Проверка наличия файла ответов
response_file = 'responses.json'
try:
    with open(response_file, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    # Если файл ответов не найден, запрашиваем данные у пользователя через консоль
    user_name = input('Введите ваше имя: ')
    time = input('Сколько лет прошло с последней встречи: ')
    item = input('Введите предмет, который вы получаете: ')
    place = input('Укажите место, за которым (или где) будете сидеть: ')

    template_data = {
        'user_name': user_name,
        'time': time,
        'item': item,
        'place': place
    }
else:
    # Если файл ответов найден, считываем данные из него
    user_name = data.get('user_name', '')
    time = data.get('time', '')
    item = data.get('item', '')
    place = data.get('place', '')

    template_data = {
        'user_name': user_name,
        'time': time,
        'item': item,
        'place': place
    }

# Запуск функции для заполнения шаблона данными и вывода результата
render_template(template_data)