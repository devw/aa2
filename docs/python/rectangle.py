class Rectangle:
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def get_area(self):
        return self.side_1 * self.side_2

    def get_perimeter(self):
        return 2 * (self.side_1 + self.side_2)


rectangle_1 = Rectangle(2, 5)
print(rectangle_1.get_area())  # 10
print(rectangle_1.get_perimeter())  # 14
