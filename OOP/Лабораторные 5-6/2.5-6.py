class Point:
    def __init__(self, name, x, y):
        # метод __init__ используется для инициализации атрибутов объекта класса Point. 
        # Он принимает три аргумента: name, x и y, которые представляют имя точки и её координаты на плоскости
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        # метод __str__ определяет, как будет представлен объект класса Point в виде строки при вызове функции str() или при его выводе. 
        # Он возвращает строку, содержащую имя точки и её координаты в формате "(x, y)"
        return f'{self.name} ({self.x}, {self.y})'

    def __eq__(self, other): # Ссылка на экземпляр other -- Объект с которым следует произвести сравнение (справа от оператора сравнения)
        if isinstance(other, Point): # сравниваем переменную: является ли она точкой? 
            # проверяет, является ли переменная other экземпляром класса Point, а затем сравнивает его атрибуты 
            # name, x и y с атрибутами текущего экземпляра класса Point 
            # Если атрибуты совпадают, то метод возвращает True, т.е. (имя, х, и у), иначе False
            return self.name == other.name and self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        # Метод __hash__ определяет хешируемость объекта класса Point, что позволяет использовать его в качестве ключа в хэш-таблицах 
        # и множествах Python. В этом методе создается кортеж из атрибутов объекта (name, x, y), который затем хешируется с помощью функции hash()
        # Таким образом, каждый объект класса Point будет иметь уникальный хеш, основанный на его имени и координатах, что позволяет использовать 
        # его в качестве ключа или элемента множества.
        return hash((self.name, self.x, self.y))

    def __add__(self, other):
        # Класс Point имеет метод __add__, который принимает другую точку и возвращает новый экземпляр класса Segment.
        # Класс Segment создается с двумя точками (start и end) и имеет метод __str__ для удобного вывода информации о отрезке.
        # Этот код позволяет складывать две точки, и результатом будет новый отрезок, соединяющий эти точки
        return Segment(self, other)

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return f"{self.point1} - {self.point2}"

# Создание экземпляров точек класса Point
p1 = Point("A", 3, 4)
p2 = Point("B", 5, 6)
p3 = Point("A", 3, 4)
p4 = Point("C", 7, 8)
p5 = Point("D", 9, 10)

print('Точка 1:', p1)
print('Точка 2:', p2)
print('Точка 3:', p3)
print('Точка 4:', p4)
print('Точка 5:', p5)
print('')
# Проверка метода __str__
print('Точка 1: ', p1)  # Вывод: A(3,4)

# Проверка метода __eq__
print('Равны ли точки А и A1: ', p1 == p3)  # Вывод: True
print('Равны ли точки А и В: ', p1 == p2)  # Вывод: False

# Проверка метода __hash__, т.е. уникальности (?)
points_set = {p1, p2, p3, p4, p5}
print('Сколько уникальных точек: ', len(points_set))  # Вывод: 4, так как p1 и p3 одинаковые

# Проверка метода __add__
segment = p1 + p2
print('Сложение двух точек с выводом их координат: ', segment)  # Вывод: A - B !!! Это не минус, а тире !!!