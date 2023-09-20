from Shape_Base import shape


class Rectangle(shape):
    def __init__(self, firstSide, secondSide):
        super().__init__(firstSide, secondSide)

    def calc_area(self):
        print(super().calc_area())
        return


