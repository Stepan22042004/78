from deq import Deq
from r2point import R2Point


class Figure():
    """ Абстрактная фигура """

    def norm_perimeter(self):
        return 0.0

    def sum_angle(self):
        return 0.0

    def area(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):

        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def sum_angle(self):
        ang = 0
        ang += R2Point.per(self.fixed_point_a, self.fixed_point_b,
                           self.p, self.q)
        ang += R2Point.per(self.fixed_point_b, self.fixed_point_c,
                           self.p, self.q)
        ang += R2Point.per(self.fixed_point_a, self.fixed_point_c,
                           self.p, self.q)
        return ang

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)

        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._norm_perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._sum_angle = R2Point.per(self.fixed_point_a,
                                      self.fixed_point_b, a, b)
        self._sum_angle += R2Point.per(self.fixed_point_b,
                                       self.fixed_point_c, a, b)
        self._sum_angle += R2Point.per(self.fixed_point_a,
                                       self.fixed_point_c, a, b)
        self._sum_angle += R2Point.per(self.fixed_point_a,
                                       self.fixed_point_b, b, c)
        self._sum_angle += R2Point.per(self.fixed_point_b,
                                       self.fixed_point_c, b, c)
        self._sum_angle += R2Point.per(self.fixed_point_a,
                                       self.fixed_point_c, b, c)
        self._sum_angle += R2Point.per(self.fixed_point_a,
                                       self.fixed_point_b, a, c)
        self._sum_angle += R2Point.per(self.fixed_point_b,
                                       self.fixed_point_c, a, c)
        self._sum_angle += R2Point.per(self.fixed_point_a,
                                       self.fixed_point_c, a, c)

        self._area = abs(R2Point.area(a, b, c))

    def norm_perimeter(self):
        return self._norm_perimeter

    def sum_angle(self):
        return self._sum_angle

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._norm_perimeter -= self.points.first().dist(
                self.points.last())
            self._sum_angle -= R2Point.per(self.fixed_point_a,
                                           self.fixed_point_b,
                                           self.points.last(),
                                           self.points.first())
            self._sum_angle -= R2Point.per(self.fixed_point_b,
                                           self.fixed_point_c,
                                           self.points.last(),
                                           self.points.first())
            self._sum_angle -= R2Point.per(self.fixed_point_a,
                                           self.fixed_point_c,
                                           self.points.last(),
                                           self.points.first())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._sum_angle -= R2Point.per(self.fixed_point_a,
                                               self.fixed_point_b,
                                               self.points.first(), t)
                self._sum_angle -= R2Point.per(self.fixed_point_b,
                                               self.fixed_point_c,
                                               self.points.first(), t)
                self._sum_angle -= R2Point.per(self.fixed_point_a,
                                               self.fixed_point_c,
                                               self.points.first(), t)
                self._norm_perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._norm_perimeter -= p.dist(self.points.last())
                self._sum_angle -= R2Point.per(self.fixed_point_a,
                                               self.fixed_point_b,
                                               self.points.last(), t)
                self._sum_angle -= R2Point.per(self.fixed_point_b,
                                               self.fixed_point_c,
                                               self.points.last(), t)
                self._sum_angle -= R2Point.per(self.fixed_point_a,
                                               self.fixed_point_c,
                                               self.points.last(), t)

                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер

            self._norm_perimeter += t.dist(self.points.first()) + t.dist(
                self.points.last())
            self._sum_angle += R2Point.per(self.fixed_point_a,
                                           self.fixed_point_b,
                                           self.points.first(), t)
            self._sum_angle += R2Point.per(self.fixed_point_b,
                                           self.fixed_point_c,
                                           self.points.first(), t)
            self._sum_angle += R2Point.per(self.fixed_point_a,
                                           self.fixed_point_c,
                                           self.points.first(), t)
            self._sum_angle += R2Point.per(self.fixed_point_a,
                                           self.fixed_point_b,
                                           self.points.last(), t)
            self._sum_angle += R2Point.per(self.fixed_point_b,
                                           self.fixed_point_c,
                                           self.points.last(), t)
            self._sum_angle += R2Point.per(self.fixed_point_a,
                                           self.fixed_point_c,
                                           self.points.last(), t)

            self.points.push_first(t)

        return self


if __name__ == "__main__":
    f = Void(1, 1, 2, 2, 3, 3)
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
