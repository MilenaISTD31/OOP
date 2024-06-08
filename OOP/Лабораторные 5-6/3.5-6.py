import math
class Segment: # Определение класса Segment, который представляет собой отрезок на плоскости.
    def __init__(self, xa, xb, ya, yb): # Конструктор класса, который инициализирует начальные и конечные координаты отрезка xa, xb для x и ya, yb для y.
        self.xa = xa # Присваивание значений координатам отрезка.
        self.xb = xb
        self.ya = ya
        self.yb = yb

    def  get_len(self): # Метод get_len вычисляет длину отрезка по формуле расстояния между двумя точками.
        # Возвращает строку с вычисленной длиной отрезка, используя функцию math.sqrt для извлечения квадратного корня:
        return f"Длина отрезка: {math.sqrt((self.xa-self.xb)** 2 + (self.ya-self.yb)** 2)}\n"

    def __str__(self): # Метод __str__ определяет, как объект будет преобразован в строку.
        return f"AB ({self.xa}, {self.ya}; {self.xb}, {self.yb})" # Возвращает строковое представление отрезка с его координатами.
    
    def __add__(self, other): # Метод __add__ определяет поведение оператора сложения + для объектов класса Segment.
        # Создание списков координат для текущего (self) и другого (other) отрезка:
        x1 = [self.xa, self.xb]
        y1 = [self.ya, self.yb]
        x2 = [other.xa, other.xb]
        y2 = [other.ya, other.yb]
        # Определение новых координат для создания ломаной линии, которая будет включать оба отрезка:
        x_new = [min(x1), max(x1), min(x2), max(x2)]
        y_new = [min(y1), max(y1), min(y2), max(y2)]
        return Broken_Line(x_new, y_new) # Возвращает новый объект класса Broken_Line, который представляет собой ломаную линию, состоящую из двух отрезков.

class Broken_Line: # Определение класса Broken_Line, который представляет собой ломаную линию.
    def __init__(self, x_coords, y_coords): # Конструктор класса, который инициализирует координаты ломаной линии.
        # Присваивание значений координатам ломаной линии:
        self.x_coords = x_coords
        self.y_coords = y_coords

    def __str__(self): # Метод __str__ определяет, как объект класса Broken_Line будет преобразован в строку.
        return f"BrokenLine ({self.x_coords}, {self.y_coords})"

# Пример использования
A = Segment(1, 2, 3, 4)
B = Segment(4, 5, 6, 7)
print(A.get_len())  # Вычисление длины отрезка
print(A)  # Приведение к строке
broken_line = A + B
print(broken_line)  # Новая ломаная линия

    

