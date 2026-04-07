#super() method

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "Not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def cal(self):
        print(f"The area of circle is : {3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, color, is_filled,width):
        super().__init__(color, is_filled)
        self.width = width

    def cal(self):
        print(f"Area of square is : {self.width * self.width}")

circle = Circle("blue",True,5)
square = Square("Green",False,4)

circle.describe()
circle.cal()
 
print("\n")

square.describe()
square.cal()