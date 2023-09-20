from Shape_Base import shape


class Square(shape):
    def __init__(self, firstSide):
        super().__init__(firstSide, firstSide)

    def calc_area(self):
        print(super().calc_area())
        return


