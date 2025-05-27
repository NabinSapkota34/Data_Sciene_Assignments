# *************************************_____TASK_5*************************************************************


# Iterate Through a Tuple and Print Types
my_tuple = (42, 3.14, "Hello", True, 2+3j)
for item in my_tuple:
    print(item, "is of type", type(item))

# Print All Items from a List with a Custom Message
cities = ["New York", "Paris", "Tokyo", "Sydney"]
for city in cities:
    print(city, "is a great place")

# Print Each Character of a String with Its Index
word = input("Enter a word: ")
for index, char in enumerate(word):
    print(f"Index {index}: {char}")

# Sum of Elements in a List
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print("Total sum is:", total)

# Count Booleans in a Tuple
mixed_tuple = (True, False, 10, "text", True, False, True)
true_count = 0
for item in mixed_tuple:
    if item is True:
        true_count += 1
print("Number of True values:", true_count)

# Check and Print Data Types from a List
mixed_list = [1, 3.14, "hello", False, [1, 2], None]
for item in mixed_list:
    print(item, "->", type(item))

# Check for Vowels in a String
user_input = input("Enter a word: ")
for char in user_input:
    if char.lower() in ("a", "e", "i", "o", "u"):
        print(char, "is a vowel")

# Print Square of Numbers from a Tuple
nums = (1, 2, 3, 4, 5)
for n in nums:
    print(f"Square of {n} is {n ** 2}")

# Print Elements of a List in Uppercase
words = ["apple", "banana", "cherry", "date", "fig"]
for word in words:
    print(word.upper())

# Count Numbers Greater Than 10 in a List
values = [5, 12, 7, 22, 3, 18]
count = 0
for val in values:
    if val > 10:
        count += 1
print("Numbers greater than 10:", count)
