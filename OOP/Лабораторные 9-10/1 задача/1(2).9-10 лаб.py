import json
import os

class Templates:
    def __init__(self, file_json=None, file_template=None, name=None, time=None, item=None, place=None) -> None:
        self.name = name
        self.time = time
        self.item = item
        self.place = place
        self.template = ''
        self.template_path = file_template
        self.json_path = file_json
        self.answers = {}
        if file_json and os.path.exists(file_json):
            self.load_answers()
        if file_template and os.path.exists(file_template):
            self.load_template()
        
    def load_template(self):
        with open(self.template_path, 'r', encoding='utf-8') as file:
            self.template = file.read()
            return self.template

    def load_answers(self):
        with open(self.json_path, 'r', encoding='utf-8') as file:
            self.answers = json.load(file)
        self.name = self.answers.get('user_name', self.name)
        self.time = self.answers.get('time', self.time)
        self.item = self.answers.get('item', self.item)
        self.place = self.answers.get('place', self.place)
        
    def get_user_input(self):
        if not self.name:
            self.name = input('Введите ваше имя: ')
        if not self.time:
            self.time = input('Сколько лет прошло с нашей последней встречи? ')
        if not self.item:
            self.item = input('Что вы хотите подарить? ')
        if not self.place:
            self.place = input('Куда вы хотите сесть? ')

    def render_template(self):
        data = {
            'user_name': self.name,
            'time': self.time,
            'item': self.item,
            'place': self.place
        }
        try:
            rendered = self.template.format(**data)
            return rendered
        except KeyError as e:
            return f'Отсутствует ключ в данных шаблона: {e}'

def main():
    template_path = 'template.txt'
    answers_path = 'answers.json'
    
    # Создаем экземпляр класса Templates
    tmpl = Templates(file_json=answers_path, file_template=template_path)
    
    # Если нет файла с ответами, запрашиваем данные у пользователя
    if not tmpl.answers:
        tmpl.get_user_input()
    
    # Рендерим и выводим шаблон
    rendered_text = tmpl.render_template()
    print('Текст:\n', rendered_text)  # Final output

if __name__ == '__main__':
    main()
