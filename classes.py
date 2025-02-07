"""
task1
Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
"""
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("write your name: ")

    def printString(self):
        print(self.input_string.upper())
str_manipulator = StringManipulator()
str_manipulator.getString()
str_manipulator.printString()
"""
the output is:
write your name: aksu
AKSU
"""

"""
task2
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print("Area of Shape:", shape.area()) 
square = Square(5)
print("Area of Square:", square.area()) 
 
"""
 the output is:
 Area of Shape: 0
Area of Square: 25
"""

"""
task3 
Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area
"""
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shape = Shape()
print("Area of Shape:", shape.area()) 
rectangle = Rectangle(5, 10)
print("Area of Rectangle:", rectangle.area()) 
"""
the output is:
Area of Shape: 0
Area of Rectangle: 50
"""

"""
task4 
Write the definition of a Point class. Objects from this class should have a

    a method show to display the coordinates of the point
    a method move to change these coordinates
    a method dist that computes the distance between 2 points

"""
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()
point2.show()

point1.move(1, -1)
point1.show()

distance = point1.dist(point2)
print("Distance between points:", distance)
"""
output:
Point coordinates: (2, 3)
Point coordinates: (5, 7)
Point coordinates: (3, 2)
Distance between points: 5.385164807134504
"""

"""
task5 
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Insufficient balance for withdrawal of {amount}.")

account = Account("Aksu", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
"""
output:
Deposited 500. New balance: 1500
Withdrew 300. New balance: 1200
Insufficient balance for withdrawal of 2000
"""

"""
task6
Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13, 15, 17, 18, 19, 20]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
"""
output is:
[2, 3, 5, 13, 17, 19]
"""
