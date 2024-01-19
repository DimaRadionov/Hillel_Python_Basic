import math
from Point import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        new_obj = super().__add__(other)
        radius = self.radius + other.radius
        return Circle(radius, new_obj.x, new_obj.y)

    def __sub__(self, other):
        if isinstance(other, Circle):
            new_obj = super().__sub__(other)
            radius = abs(self.radius - other.radius)
            return Circle(radius, new_obj.x, new_obj.y)
        return Point()

    def area(self):
        return round(math.pi * (self.radius ** 2), 3)


circle_1 = Circle(5, 7)
print(circle_1)
print(circle_1.area())
print(circle_1.distance_from_origin())

circle_2 = Circle(5, 1, 2)
print(circle_1 == circle_2)
print(circle_1 + circle_2)

circle_3 = Circle(3, 2, 1)
print(circle_1 - circle_3)
