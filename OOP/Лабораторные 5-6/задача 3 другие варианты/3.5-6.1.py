import math
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.name} ({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Point): 
            return self.name == other.name and self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.name, self.x, self.y))

    def __add__(self, other):
        return Segment(self, other)

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def  get_len(self):
        return f"Длина отрезка: {math.sqrt((self.point1.x-self.point2.x)** 2 + (self.point1.y-self.point2.y)** 2)}\n"

    def __str__(self):
        return f"AB ({self.point1}, {self.point2})"
    
    def __add__(self, other):
        return Broken_Line(self, other)


class Broken_Line:
    def __init__(self, Points):
        if len(Points) < 3:
            raise ValueError('Точек должно быть не меньше 3')
        self.Points = [i for i in Points]
    
    def __str__(self):
        r = ', '.join(str(i) for i in  self.Points)
        return f"BrokenLine({r})"

# Создание экземпляров точек класса Point
Point_1 = Point('M', 2, 3)
Point_2 = Point('A', 4, 5)
Point_3 = Point('Y', 1, 6)
segment_1 = Segment(Point_1, Point_2)
a = [Point_1, Point_2, Point_3]
broken_line_1 = Broken_Line(a)
print('Точка №1 : ', Point_1, 'Точка №2 : ', Point_2, 'Точка №3 : ', Point_3, 'Отрезок: ', segment_1, 'Ломаная линия: ', broken_line_1)


