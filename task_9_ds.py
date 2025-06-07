from functools import reduce
from abc import ABC, abstractmethod

# 1. Return product of any count of numbers
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

# 2. Return length of a string
def string_length(s):
    return len(s)

# 3. Check if number is divisible by 7
def divisible_by_7(n):
    return n % 7 == 0

# 4. Return maximum value from a list
def max_in_list(lst):
    return max(lst)

# 5. Map: square only even numbers
squared_evens = list(map(lambda x: x**2 if x % 2 == 0 else x, [1, 2, 3, 4, 5]))

# 6. Filter: extract even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8]))

# 7. Reduce: product of list
product_list = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

# 8. Convert strings to uppercase using map()
uppercase_strings = list(map(lambda s: s.upper(), ["apple", "banana", "cherry"]))

# 9. Filter words with length > 3
long_words = list(filter(lambda w: len(w) > 3, ["hi", "hello", "world", "yes"]))

# 10. Lambda: add 10
add_10 = lambda x: x + 10

# 11. Lambda: cube of number
cube = lambda x: x ** 3

# 12. Lambda: check divisible by 9
div_by_9 = lambda x: x % 9 == 0

# 13. Lambda with map: double each element
doubled = list(map(lambda x: x * 2, [2, 4, 6, 8]))

# 14. Lambda with filter: numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, [1, 4, 6, 7, 9]))

# 15. Mobile class
class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# 16. Student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# 17. Rectangle class with area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# 18. Person class with private salary
class Person:
    def __init__(self, salary):
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary

# 19. Two classes with describe method
class Dog:
    def describe(self):
        print("This is a Dog.")

class Cat:
    def describe(self):
        print("This is a Cat.")

# 20. Person class with display method
class PersonInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# 21. Call area() method from different shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

def print_area(shape):
    print(shape.area())

# 22. Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

# 23. Calculator class
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b if b != 0 else "Cannot divide by zero"

# 24. ABC abstract class for Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2

class RectangleShape(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

# 25. Create a file, write and read
with open("sample.txt", "w") as f:
    f.write("Hello, Python!")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# 26. Try-except-finally
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution completed")

# 27. CustomException for odd number
class CustomException(Exception):
    pass

def check_even(n):
    if n % 2 != 0:
        raise CustomException("Odd number not allowed")
    else:
        print("Even number accepted")

# 28. Divide with zero-handling
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Denominator cannot be zero")
