#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void, Figure


print("Заданные точки")
Figure.fixed_point_a = R2Point()
Figure.fixed_point_b = R2Point()
Figure.fixed_point_c = R2Point()
print("\nТочки плоскости")


f = Void()
try:
    while True:
        f = f.add(R2Point())
        print(f"S={f.area()}, P_norm={f.norm_perimeter()}, A={f.sum_angle()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
