import math
# Animal Base Class
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound.")

    def __str__(self):
        return f"Animal Name: {self.name}"

# Dog Class
class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says: Woof! Woof!")

# Cat Class
class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says: Meow! Meow!")

# Shape Base Class
class Shape:

    def __init__(self):
        pass

    def area(self):
        return 0

# Rectangle Class
class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Circle Class
class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Animal Objects
animals = []
number = int(input("How many animals do you want to create? "))
for i in range(number):
    print(f"\nAnimal {i+1}")
    animal_type = input("Enter Animal Type (Dog/Cat): ").strip().lower()
    name = input("Enter Animal Name: ")
    if animal_type == "dog":
        animals.append(Dog(name))
    elif animal_type == "cat":
        animals.append(Cat(name))
    else:
        print("Invalid Animal Type!")
        print("Creating a Dog by default.")
        animals.append(Dog(name))

print("\n\n ANIMAL DETAILS")
for animal in animals:
    print(animal)
print("\n\n POLYMORPHISM")
for animal in animals:
    animal.speak()
    
# Rectangle
print("\n\n RECTANGLE")
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
rectangle = Rectangle(length, width)
print("Area of Rectangle =", rectangle.area())

# Circle
print("\n\n CIRCLE")
radius = float(input("Enter Radius: "))
circle = Circle(radius)
print("Area of Circle =", round(circle.area(), 2))