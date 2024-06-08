import math # импорт библиотЭки

class Point: # класс для точек
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self): #возвращаем имя и координаты точки
        return f'{self.name} ({self.x}, {self.y})'

    def __eq__(self, other): # см. предыдущую задачу
        if isinstance(other, Point): 
            return self.name == other.name and self.x == other.x and self.y == other.y
        return False

    def __hash__(self): # см. предыдущую задачу
        return hash((self.name, self.x, self.y))

    def __add__(self, other): # см. предыдущую задачу
        return Segment(self, other)

class Segment: # класс для отрезков. Пояснения в предыдущих заданиях этой лабораторной
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def  get_len(self):
        return f'Длина отрезка: {math.sqrt((self.point1.x-self.point2.x)** 2 + (self.point1.y-self.point2.y)** 2)}'

    def __str__(self):
        return f'Отрезок {self.point1.name}{self.point2.name} ({self.point1.x}, {self.point1.y}; {self.point2.x}, {self.point2.y})'
    
    def __add__(self, other):
        return Broken_Line([self.point1, self.point2, other.point1, other.point2])


class Broken_Line: # класс для ломаной. она создается при наличии не менее 3-х точек, поэтому сразу же прописываем это условие
    def __init__(self, Points):
        if len(Points) < 3:
            raise ValueError('Точек должно быть не меньше 3')
        self.Points = [i for i in Points]
    
    def __str__(self): # эта штучка пречисляет точки, которые входят в ломаную
        r = ', '.join(str(i) for i in  self.Points)
        return f'Ломаная: ({r})'
    
    def get_len(self): # вычисление длины ломаной. определение метода get_len, который будет вызываться для объекта класса
        total_length = 0 # инициализация переменной total_length значением 0. Эта переменная будет использоваться для накопления общей длины ломаной.
        for i in range(len(self.Points) - 1): # начало цикла for, который будет итерировать по индексам списка self.Points. 
            #Список self.Points содержит объекты, представляющие точки ломаной. -1 в range гарантирует, что цикл не выйдет за пределы списка, так как 
            # длина отрезка вычисляется между последовательными парами точек.
            total_length += math.sqrt((self.Points[i].x - self.Points[i + 1].x)**2 + (self.Points[i].y - self.Points[i + 1].y)**2) # вычисление длины отрезка между двумя точками. Это делается путем вычисления евклидова расстояния между точками i и i + 1
        return total_length
    
    # def  get_len(self):
    #   return f'Длина отрезка: {math.sqrt((self.point1.x-self.point2.x)** 2 + (self.point1.y-self.point2.y)** 2)}\n' !!!ЭТО ИЗ ОТРЕЗКА!!!
    
    def __add__(self, other): 
        if isinstance(other, Point): # - проверка, является ли объект other экземпляром класса Point. Это гарантирует, что к ломаной можно добавлять только точки.
            return Broken_Line(self.Points + [other]) # если other является точкой, метод создает новый объект Broken_Line, который содержит все точки текущей ломаной (список self.Points) плюс новую точку (other). 
        # Здесь предполагается, что у класса Broken_Line есть конструктор, который принимает список точек.
        else:
            raise TypeError('Можно добавлять только точки!!!') # генерируется исключение TypeError с сообщением о том, что к ломаной можно добавлять только точки.

# Создание точек 
Point_1 = Point('M', 2, 3)
Point_2 = Point('A', 4, 5)
Point_3 = Point('Y', 1, 6)
Point_4 = Point('B', 7, 9)
Point_5 = Point('D', 8, 10)

# Предыдущие задачи
segment_1 = Segment(Point_1, Point_2)
a = [Point_1, Point_2, Point_3]
broken_line_1 = Broken_Line(a)
print('Точка №1 : ', Point_1, 'Точка №2 : ', Point_2, 'Точка №3 : ', Point_3, 'Отрезок: ', segment_1, broken_line_1) # Точка №1 :  M (2, 3) Точка №2 :  A (4, 5) Точка №3 :  Y (1, 6) Отрезок:  Отрезок MA (2, 3; 4, 5) Ломаная: (M (2, 3), A (4, 5), Y (1, 6))

# Вычисление длины ломаной 
print('Длина ломаной_1:', broken_line_1.get_len()) # Длина ломаной_1: 5.99070478491457

# Создание отрезков
segment1 = Point_1 + Point_2
segment2 = Point_3 + Point_4

# Вычисление длины отрезков
print('')
print(segment1.get_len())  # 2.8284271247461903
print(segment2.get_len())  # 6.708203932499369

# Сложение отрезков в ломаную
broken_line_2 = segment1 + segment2
print('')
# Здесь используем перечисление через запятую методом __str__ в классе Broken_Line
print(broken_line_2)  # Ломаная: (M (2, 3), A (4, 5), Y (1, 6), B (7, 9))
print('Длина ломаной_2:', broken_line_2.get_len())  # Длина ломаной_2: 12.69890871741394

# Добавление  - сложение ломаной и точки ?
# Как я поняла сложениеи с точкой - это добавление точки к ломаной
s3 = broken_line_2 + Point_5
print('')
print(s3)  # Ломаная: (M (2, 3), A (4, 5), Y (1, 6), B (7, 9), D (8, 10))
