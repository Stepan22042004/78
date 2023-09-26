from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


# Тесты для новой программы
class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure.fixed_point_a = R2Point(0, 0)
        Figure.fixed_point_b = R2Point(5, 0)
        Figure.fixed_point_c = R2Point(0, 5)
        self.f = Void()

    def test_1(self):
        assert self.f.sum_angle() == 0


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure.fixed_point_a = R2Point(0, 0)
        Figure.fixed_point_b = R2Point(5, 0)
        Figure.fixed_point_c = R2Point(0, 5)
        self.f = Point(
            R2Point(
                -1.0, 1.0))

    def test_1(self):
        assert self.f.sum_angle() == 0


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure.fixed_point_a = R2Point(0, 0)
        Figure.fixed_point_b = R2Point(5, 0)
        Figure.fixed_point_c = R2Point(0, 5)
        self.f = Segment(
            R2Point(
                -1.0, 1.0), R2Point(
                1.0, -1.0))

    def test_1(self):
        assert self.f.sum_angle() == approx(90)
    #   добавление точки может его изменить

    def test_2(self):
        assert self.f.add(R2Point(1, 1)).sum_angle() == approx(270)


class TestPolygon_0:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure.fixed_point_a = R2Point(0, 0)
        Figure.fixed_point_b = R2Point(5, 0)
        Figure.fixed_point_c = R2Point(0, 5)
        self.f = Polygon(
            R2Point(
                1.0, 1.0), R2Point(
                -1.0, 1.0), R2Point(
                1.0, -1.0))

    def test_1(self):
        assert self.f.sum_angle() == approx(270)
    #   добавление точки может его изменить

    def test_2(self):
        assert self.f.add(R2Point(-1, -1)).sum_angle() == approx(180)


class TestPolygon_1:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Figure.fixed_point_a = R2Point(0, 0)
        Figure.fixed_point_b = R2Point(5, 0)
        Figure.fixed_point_c = R2Point(0, 5)
        self.f = Polygon(
            R2Point(
                -1.0, 1.0), R2Point(
                -1.0, -1.0), R2Point(
                1.0, -1.0))

    def test_1(self):
        assert self.f.sum_angle() == approx(90)
    #   добавление точки может его изменить

    def test_2(self):
        assert self.f.add(R2Point(-2, -2)).sum_angle() == approx(90)
