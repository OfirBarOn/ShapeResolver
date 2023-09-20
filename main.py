from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle
from Circle import Circle
from Hexagon import Hexagon

r1 = Rectangle(3, 5)
# r1.calc_area()
print(r1.__str__())
print(type(r1))

c1 = Circle(5)
# c1.get_area()

h1 = Hexagon(5)
# h1.calc_area()

t1 = Triangle(2, 3)
# t1.calc_area()

s1 = Square(5)
# s1.calc_area()
