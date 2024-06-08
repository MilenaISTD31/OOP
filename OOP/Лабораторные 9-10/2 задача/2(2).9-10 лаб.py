from jinja2 import Template

# Запрос данных у пользователя
character1_name = input('Введите имя первого персонажа: ')
character2_name = input('Введите имя второго персонажа: ')
competition_type = input('Введите вид соревнования: ')
character1_score = int(input(f'Введите характеристику {character1_name} в {competition_type}: '))
character2_score = int(input(f'Введите характеристику {character2_name} в {competition_type}: '))

# Шаблон текста
template_text = '''
В соревновании по {{ competition_type }} участвовали {{ character1_name }} и {{ character2_name }}.
{% if character1_score > character2_score %}
Победил {{ character1_name }} с результатом {{ character1_score }}.
{% elif character2_score > character1_score %}
Победил {{ character2_name }} с результатом {{ character2_score }}.
{% else %}
Ничья! Оба персонажа набрали по {{ character1_score }} очков.
{% endif %}
'''

# Создание шаблона и рендеринг
template = Template(template_text)
rendered_text = template.render(
    character1_name=character1_name,
    character2_name=character2_name,
    competition_type=competition_type,
    character1_score=character1_score,
    character2_score=character2_score
)

# Вывод результата
print(rendered_text)