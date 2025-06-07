from functools import reduce

# 1. Encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age


# 2. Polymorphism
class Student:
    def details(self):
        print("Student: John, Grade: A")

class Teacher:
    def details(self):
        print("Teacher: Mr. Smith, Subject: Math")

def show_details(obj):
    obj.details()


# 3. Single Inheritance
class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    def wheels(self):
        print("Two wheels")


# 4. Multiple Inheritance
class Singer:
    def sing(self):
        print("Singing...")

class Dancer:
    def dance(self):
        print("Dancing...")

class Performer(Singer, Dancer):
    pass


# 5. Hierarchical Inheritance
class Appliance:
    def power_on(self):
        print("Appliance powered on")

class WashingMachine(Appliance):
    def wash(self):
        print("Washing clothes")

class Microwave(Appliance):
    def heat(self):
        print("Heating food")


# 6. Polymorphism Using Loop
class Pen:
    def write(self):
        print("Writing with a pen")

class Pencil:
    def write(self):
        print("Writing with a pencil")

# 7. Use Encapsulation to Protect Age
class SafePerson:
    def __init__(self):
        self.__age = 0
    
    def set_age(self, age):
        if age < 0:
            print("Invalid age")
        else:
            self.__age = age
    
    def get_age(self):
        return self.__age


# 8. Company Structure
class Company:
    def company_name(self):
        print("Company: TechCorp")

class Department(Company):
    def department_name(self):
        print("Department: IT")

class Employee(Department):
    def employee_name(self):
        print("Employee: Alice")


# 9. Lambda to check if number is positive
is_positive = lambda x: x > 0
print(is_positive(5))    # True
print(is_positive(-3))   # False
print(is_positive(0))    # False

# 10. Lambda to get first character
first_char = lambda s: s[0] if s else ''
print(first_char("apple"))  # 'a'

# 11. Add 10 to list elements
nums = [1, 2, 3, 4, 5]
plus_ten = list(map(lambda x: x + 10, nums))
print(plus_ten)  # [11, 12, 13, 14, 15]

# 12. Length of each word
words = ["apple", "banana", "kiwi"]
lengths = list(map(lambda w: len(w), words))
print(lengths)  # [5, 6, 4]

# 13. Filter > 50
nums2 = [10, 55, 60, 23, 90]
greater_50 = list(filter(lambda x: x > 50, nums2))
print(greater_50)  # [55, 60, 90]

# 14. Join letters using reduce
letters = ['P', 'Y', 'T', 'H', 'O', 'N']
word = reduce(lambda a, b: a + b, letters)
print(word)  # "PYTHON"

# Demonstration Code

# Encapsulation usage
p = Person("Bob", 30)
print(p.get_name(), p.get_age())
p.set_name("Alice")
p.set_age(25)
print(p.get_name(), p.get_age())

# Polymorphism
s = Student()
t = Teacher()
show_details(s)
show_details(t)

# Single Inheritance
b = Bike()
b.start()
b.wheels()

# Multiple Inheritance
perf = Performer()
perf.sing()
perf.dance()

# Hierarchical Inheritance
wm = WashingMachine()
mw = Microwave()
wm.power_on()
wm.wash()
mw.power_on()
mw.heat()

# Polymorphism in loop
items = [Pen(), Pencil()]
for i in items:
    i.write()

# SafePerson Age Protection
sp = SafePerson()
sp.set_age(-5)  # Should print Invalid age
sp.set_age(35)
print("Age is:", sp.get_age())

# Company Structure
emp = Employee()
emp.company_name()
emp.department_name()
emp.employee_name()
