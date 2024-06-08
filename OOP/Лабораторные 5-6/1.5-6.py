class Point:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

class Segment:
    def __init__(self, Point_1, Point_2):
        self.Point_1 = Point_1
        self.Point_2 = Point_2

class Broken_Line:
    def __init__(self, Points):
        if len(Points) < 3:
            raise ValueError('Точек должно быть не меньше 3')
        self.Points = [i for i in Points]

Point_1 = Point(2, 3, 'M')
Point_2 = Point(1, 5, 'A')
Point_3 = Point(4, 6, 'Y')
segment_1 = Segment(Point_1, Point_2)
a = [Point_1, Point_2, Point_3]
broken_line_1 = Broken_Line(a)
print('Точка №1 : ', Point_1, 'Точка №2 : ', Point_2, 'Точка №3 : ', Point_3, 'Отрезок: ', segment_1, 'Ломаная линия: ', broken_line_1)
