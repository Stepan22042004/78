#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon, Figure

print("Заданные точки")
Figure.fixed_point_a = R2Point()
Figure.fixed_point_b = R2Point()
Figure.fixed_point_c = R2Point()
print("Точки оболочки")


def void_draw(self, tk):
    tk.draw_line(self.fixed_point_b, self.fixed_point_a)
    tk.draw_line(self.fixed_point_b, self.fixed_point_c)
    tk.draw_line(self.fixed_point_c, self.fixed_point_a)


def point_draw(self, tk):
    tk.draw_point(self.p)
    tk.draw_line(self.fixed_point_b, self.fixed_point_a)
    tk.draw_line(self.fixed_point_b, self.fixed_point_c)
    tk.draw_line(self.fixed_point_c, self.fixed_point_a)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)
    tk.draw_line(self.fixed_point_b, self.fixed_point_a)
    tk.draw_line(self.fixed_point_b, self.fixed_point_c)
    tk.draw_line(self.fixed_point_c, self.fixed_point_a)


def polygon_draw(self, tk):
    tk.draw_line(self.fixed_point_b, self.fixed_point_a)
    tk.draw_line(self.fixed_point_b, self.fixed_point_c)
    tk.draw_line(self.fixed_point_c, self.fixed_point_a)
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()


try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        print(
            f"S = {f.area()}, P = {f.norm_perimeter()}, D = {f.sum_angle()}\n")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
