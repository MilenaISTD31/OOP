class Point:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def koordinate(self):
        print("Координата точки", self.name, "по оси x: ", self.x)
        print("Координата точки", self.name, "по оси y: ", self.y)
 
x = input("Введите значение x:\n")
y = input("Введите значение y:\n")
name = input("Введите имя точки:\n")
 
tochka = Point(x, y, name)
tochka.koordinate()
print('')

class Segment:
    def __init__(self, Point_1, Point_2):
        self.Point_1 = Point_1
        self.Point_2 = Point_2

    def koordinate(self):
        print("Отрезок с точками", self.Point_1, "и", self.Point_2)

point_x = input("Введите значение x для отрезка:\n")
point_y = input("Введите значение y для отрезка:\n")
 
segment = Segment(point_x, point_y)
segment.koordinate()
print('')

class Broken_Line:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError('Точек должно быть не меньше 3')
        self.points = points

    def koordinate(self):
        print("Ломанная с точками", self.points)

point_x1 = input("Введите значение x1 для ломанной:\n")
point_x2 = input("Введите значение x2 для ломанной:\n")
point_x3 = input("Введите значение x3 для ломанной:\n")
 
broken_line = Broken_Line([point_x1, point_x2, point_x3])
broken_line.koordinate()

    