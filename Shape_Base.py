class shape:
    def __init__(self, firstSide, secondSide):
        self.side1 = firstSide
        self.side2 = secondSide

    def calc_area(self):
        return self.side1 * self.side2
