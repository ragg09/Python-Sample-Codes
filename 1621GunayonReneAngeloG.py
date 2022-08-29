#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area
class Circle():
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return (self.rad**2)*3.14

NewCircle = input("Number: ")
NewCircle = Circle(NewCircle)
print(NewCircle.area())
