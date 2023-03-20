class Shape:
    shape_name = "shape"

    def __init__(self, bgColor, brColor):
        self.bgColor = bgColor
        self.brColor = brColor

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

    def description(self):
        return f"The {Shape.shape_name} of the object is a {self.shape_name}, and its area and perimeter are equivalent to {self.getArea()} and {self.getPerimeter()}, respectively. Its background color is {self.bgColor}"


class Circle(Shape):
    shape_name = "circle"

    def __init__(self,  bgColor, brColor, radius):
        super().__init__(bgColor, brColor)
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getPerimeter(self):
        return round(2 * 3.14 * self.radius, 2)


class Square(Shape):
    shape_name = "square"

    def __init__(self,  bgColor, brColor, side):
        super().__init__(bgColor, brColor)
        self.side = side

    def getArea(self):
        return self.side * self.side

    def getPerimeter(self):
        return self.side * 4


circle = Circle("red", "yellow", 10)
square = Square("green", "yellow", 10)

print(circle.description())
# The shape of the object is a circle, and its area and perimeter are equivalent to 314.0 and 62.8, respectively.
# Its background color is red
print(square.description())
# The shape of the object is a square, and its area and perimeter are equivalent to 100 and 40, respectively.
# Its background color is green
