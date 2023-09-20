import math
from Shape_Base import shape


class Circle(shape):
    def __init__(self, firstSide):
        super().__init__(firstSide, firstSide)

    def get_area(self):
        area = math.pi * self.side1 ** 2
        print(area)
        return

