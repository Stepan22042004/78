import math


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Векторное произведение
    @staticmethod
    def vec(a, b, c):
        return 2*R2Point.area(a, b, c)

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    # Находит пересечение отрезков, если оно существует
    @staticmethod
    def per(a, b, c, d):
        if(R2Point.vec(d, a, c)*R2Point.vec(d, b, c) <= 0 and
           R2Point.vec(a, b, c)*R2Point.vec(a, b, d) <= 0):

            a1 = a.y-b.y
            b1 = b.x-a.x
            a2 = c.y-d.y
            b2 = d.x-c.x
            D = a1*b2-a2*b1
            if D != 0:
                l1_x = a.x - b.x
                l2_x = c.x - d.x
                l1_y = a.y - b.y
                l2_y = c.y - d.y
                ang = math.degrees(math.acos(abs(l1_x * l2_x + l1_y * l2_y) /
                                   (math.sqrt(l1_x**2 + l1_y**2) * math.sqrt(
                                       l2_x**2 + l2_y**2))))
                return ang
            else:
                return 0
        else:
            return 0


if __name__ == "__main__":

    a, b, c, d, e = R2Point(0, 0), R2Point(
        1, 0), R2Point(0, 1), R2Point(0, 0), R2Point(1, 0)
    print(R2Point.perim(a, b, c, d, e))
