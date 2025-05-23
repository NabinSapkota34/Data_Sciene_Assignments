# ********************************TASK3***********************************

# Integer & Float Mix

a = 2
b = 3.12

result1 = a + b
result2 = b - a
result3 = a * b
result4 = b / a

print("Addition:", result1, "Type:", type(result1))
print("Subtraction:", result2, "Type:", type(result2))
print("Multiplication:", result3, "Type:", type(result3))
print("Division:", result4, "Type:", type(result4))


# Large Integers & Type

large_int = 9876543210123456789
print("Large Integer:", large_int)
print("Type of large_int:", type(large_int))


# Complex Number Basics

z = 3 + 4j
print("Complex number z:", z)
print("Real part:", z.real)
print("Imaginary part:", z.imag)
print("Type of z:", type(z))
z2 = 1 + 2j # Arithmetic with another complex number
result = z + z2
print("Addition of complex numbers:", result)


# Boolean from Comparisons

m=10;
n=15;
status = m>n 
print(status, type(status))
status = (m != n) 
print(status, type(status))


# String Creation & Indexing
text = "HelloWorld";
print(text[0],text[-1])
print(len(text))

#string slicing
lang = "PythonProgramming"

print("Substring [2:8]:", lang[2:8])
print("Substring [:5]:", lang[:5])
print("Reversed string:", lang[::-1])


# String Methods
phrase = " Hello, Python World! "

stripped = phrase.strip()
uppercased = phrase.upper()
replaced = phrase.replace("Python", "Java")


print("Original phrase:", repr(phrase))
print("After strip():", repr(stripped))
print("After upper():", repr(uppercased))
print("After replace():", repr(replaced))

# String Formatting
name = "Rajesh"
score = 95
print(name + " scored " + str(score) + " points.")
print(f"{name} scored {score} points.")
print("{} scored {} points.".format(name, score))


# Boolean Operations in Expressions
result = not(True and False) or (5 > 3)
print("Boolean result:", result) 

# List Creation & Access
nums = [12, 45, 33, 28, 91]
print("First item:", nums[0])
print("Middle item:", nums[len(nums)//2])
print("Last item:", nums[-1])

# List Insertion & Deletion
nums2 = [10, 20, 30, 40]
nums2.insert(2, 25)
nums2.pop()
print("Updated list:", nums2)

# List Slicing
letters = ["a", "b", "c", "d", "e"]
print("Slice ['b', 'c', 'd']:", letters[1:4])
print("Omitting first and last:", letters[1:-1])

# Sorting & Reversing
rand_nums = [14, 3, 77, 8, 25]
rand_nums.sort()
print("Sorted:", rand_nums)
rand_nums.reverse()
print("Reversed:", rand_nums)

# Combining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Combined using +:", combined)
list1.extend(list2)
print("Combined using .extend():", list1)

# Aggregating List Values
floats = [2.5, 3.6, 1.2, 5.0]
print("Sum:", sum(floats))
print("Min:", min(floats))
print("Max:", max(floats))

# Tuple Creation
t = (10, 20, "Hello", True)
print("Tuple:", t)
print("Type:", type(t))

# Tuple Indexing & Slicing
print("First two:", t[:2])
print("Last element:", t[-1])

# Tuple Unpacking
t2 = ("Tom", 25, "Engineer")
name, age, profession = t2
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# Attempt Tuple Mutation
try:
    t[0] = 999
except TypeError as e:
    print("Tuple mutation error:", e)  # Tuples are immutable

# Set Creation & Membership
my_set = {1, 3, 5, 7}
print(5 in my_set)
print(2 not in my_set)

# Add & Remove Elements
my_set.add(9)
my_set.remove(3)
print("Updated set:", my_set)

# Set Operations
setA = {1, 2, 3}
setB = {3, 4, 5}
print("Union:", setA | setB)
print("Intersection:", setA & setB)
print("Difference (A - B):", setA - setB)

# Check Unique Values
vals = [1, 2, 2, 3, 3, 3, 4]
unique_vals = set(vals)
print("Original list:", vals)
print("Set:", unique_vals)

# Frozenset Creation
frozen = frozenset([2, 4, 4, 6])
print("Frozenset:", frozen)

# Immutability Demonstration
try:
    frozen.add(8)
except AttributeError as e:
    print("Frozenset add error:", e)  # Frozensets are immutable

# Frozenset Use as a Dictionary Key
my_dict = {frozenset([1, 2, 3]): "value"}
print("Dictionary with frozenset key:", my_dict)

# Dictionary Creation & Access
student = {"name": "Ramesh", "age": 20, "grade": "A"}
print("Name:", student["name"])
print("Age:", student["age"])

# Adding & Updating Keys
student["city"] = "Kathmandu"
student["age"] = 21
print("Updated student:", student)

# Removing Keys
del student["grade"]
print("After removing grade:", student)

# Nested Dictionary Example
record = {"id": 101, "info": {"name": "Bob", "dept": "IT"}}
print("Department:", record["info"]["dept"])

# Operator Precedence
a, b, c = 4, 2, 5
print("a + b * c:", a + b * c)  # 4 + (2*5) = 14
print("(a + b) * c:", (a + b) * c)  # (4+2)*5 = 30

# Modulo & Floor Division
x, y = 17, 4
print("x % y:", x % y)  # Remainder
print("x // y:", x // y)  # Quotient

# Power Operator
print("2 ** 3:", 2 ** 3)
print("3 ** 4:", 3 ** 4)
print("Sum of both:", 2**3 + 3**4)

# String Comparison
print("apple" < "banana")
print("apple" > "banana")
print("apple" == "banana")

# Mixed Type Comparison
print(5 == 5.0)  # True, same value
print(5 is 5.0)  # False, different types

# Chain Comparisons
print("2 < 3 < 5:", 2 < 3 < 5)  # True

# Logical and
p, q = True, False
print("p and q:", p and q)
age = 20
has_ID = True
print("(age > 18) and (has_ID):", (age > 18) and (has_ID))

# Logical or
print("p or q:", p or q)

# Logical not
r = (10 > 5)
print("r:", r)
print("not r:", not r)

# Using len()
lst = [1, 2, 3, 4, 5, 6, 7]
print("Length:", len(lst))

# Using type()
print(type(10), type(10.5), type("ten"), type(True), type(3+2j))
# int, float, str, bool, complex

# Using abs()
print(abs(10), abs(-10), abs(-3.5))  # Absolute values

# Using round()
print(round(3.14159, 2))  # 3.14
print(round(2.5))  # 2 (rounds to even in Python)

# Using sum(), max(), min()
values = [7, 2, 9, 4]
print("Sum:", sum(values))
print("Max:", max(values))
print("Min:", min(values))

# Using sorted()
vals = (3, 1, 4, 2)
print("Sorted:", sorted(vals))
print("Original tuple:", vals)

# Using any() / all()
bools = [True, False, True]
print("any:", any(bools))
print("all:", all(bools))

# Storing Booleans from Comparisons
a = (10 > 3)
b = (5 == 5)
print("a and b:", a and b)
print("a or b:", a or b)

# Multiline String & Counting
hobby = """
I enjoy painting and creating abstract artworks. Art is a form of relaxation.
"""
print("Count of 'a':", hobby.lower().count('a'))  # Case-insensitive

# Advanced String Slicing
s = "ABCDEFGHIJ"
print("Every second character:", s[::2])  # "ACEGI"
print("Reverse step slice:", s[::-1])

# Casefold vs. Lower
s1 = "Case"
s2 = "case"
print("s1 == s2:", s1 == s2)
print("s1.casefold() == s2.casefold():", s1.casefold() == s2.casefold())

# Formatted Printing
name = "Ramesh"
product = "Notebook"
quantity = 2
price = 12.50
print(f"{name} purchased {quantity} {product} for a total of ${quantity * price}.")

# Type Conversion Chain
str_input = "0"
flt = float(str_input)
bl = bool(flt)
print("Float:", flt, "Boolean:", bl)

# String List Sorting
fruits = ["apple", "banana", "cherry"]
print("Descending sorted:", sorted(fruits, reverse=True))
fruits.reverse()
print("Reversed list:", fruits)

# Insert Using Slicing
lst = [2, 5, 7, 1, 9]
lst[1:1] = [4]
print("After slicing insert:", lst)

# Indexing Within a Mixed List
info = ["John", 28, True, 4500.75]
print("Name:", info[0], "Salary:", info[3])

# Tuple Concatenation & Replication
t1 = (1, 2)
t2 = (3, 4)
print("Concatenated:", t1 + t2)
print("Replicated:", t1 * 3)

# Single-Element Tuple
print("Single-element tuple:", (42,), "Type:", type((42,)))
print("Not a tuple:", (42), "Type:", type((42)))

# Intersection & Union
setA = {1, 2, 3, 4}
setB = {1, 2, 3}
print("Intersection:", setA & setB)
print("Union:", setA | setB)

# Subset and Superset
print("setB is subset of setA:", setB.issubset(setA))
print("setA is superset of setB:", setA.issuperset(setB))

# Countries and Capitals
capitals = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome"}
print("Keys:", capitals.keys())
print("Values:", capitals.values())
print("Items:", capitals.items())

# Summing Dictionary Values
numbers = {"x": 4, "y": 10, "z": 6}
print("Sum of values:", sum(numbers.values()))


