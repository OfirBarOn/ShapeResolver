import math
from Shape_Base import shape


class Hexagon(shape):
    def __init__(self, firstSide):
        super().__init__(firstSide, firstSide)

    def calc_area(self):
        try:
            area = ((3 * math.sqrt(3)) / 2) * self.side1 ** 2
        except:
            pass
        print(area)
        return



