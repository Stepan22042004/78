from pytest import approx
from r2point import *

class TestR2Point:

    def test_perim00(self):
        a = R2Point(0.0, 0.0)
        b = R2Point(1.0, 0.0)
        c = R2Point(0.0, 1.0)
        p = R2Point(0.0, 0.0)
        q = R2Point(0.0, 1.0)
        assert R2Point.perim(a, b, c, p, q) == approx(1.0)
        
    def test_perim01(self):
        a = R2Point(0.0, 0.0)
        b = R2Point(1.0, 0.0)
        c = R2Point(0.0, 1.0)
        p = R2Point(0.0, 0.0)
        q = R2Point(0.0, -1.0)
        assert R2Point.perim(a, b, c, p, q) == approx(0.0)