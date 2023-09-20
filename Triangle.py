from Shape_Base import shape


class Triangle(shape):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calc_area(self):
        print(0.5 * super().calc_area())
        return


