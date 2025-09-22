class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of Circle = πr²")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = l × b")

class Triangle(Shape):
    def area(self):
        print("Area of Triangle = 0.5 × b × h")

# Same method name, different behavior
for shape in [Circle(), Rectangle(), Triangle()]:
    shape.area()