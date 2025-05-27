# *************************************_____TASK_4*************************************************************

# Even or Odd Checker
user = int(input("Enter a number: "))

if user % 2 == 0:
    print("Even")
else:
    print("Odd")


#Positive, Negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Grade Categorizer
usr = int(input("Enter the number from 0 to 100: "))

if 90 <= usr <= 100:
    print("Grade A")
elif 80 <= usr <= 89:
    print("Grade B")
elif 70 <= usr <= 79:
    print("Grade C")
else:
    print("Fail")


# Multiples of 3 and 5

num1 = int(input("Enter the integer: "))
for i in range(1, num1 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Multiple of both")
    elif i % 3 == 0:
        print("Multiple of 3")
    elif i % 5 == 0:
        print("Multiple of 5")
    else:
        print(i)


# Simple Password Check
passw = input("Enter the password: ")
if passw == "Secret":
    print("Access Granted")
else:
    print("Access Denied")


# Count Vowels in a String

user1 = input("Enter a string: ")
count = 0

for i in user1:
    if i.lower() in ("a", "e", "i", "o", "u"):
        count += 1

print("Number of vowels:", count)


# Smallest of Three Numbers

user2 = int(input("Enter number 1: "))
user3 = int(input("Enter number 2: "))
user4 = int(input("Enter number 3: "))

if user2 < user3 and user2 < user4:
    print("The smallest number is:", user2)
elif user3 < user2 and user3 < user4:
    print("The smallest number is:", user3)
else:
    print("The smallest number is:", user4)


# Simple Menu Selection
def display_menu():
    print("\nMenu:")
    print("1. Start")
    print("2. Settings")
    print("0. Exit")

def handle_choice(choice):
    if choice == "1":
        print("Game starting...")
    elif choice == "2":
        print("Opening settings...")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Invalid choice.")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    handle_choice(choice)
    if choice == "0":
        break


# Print Numbers from 1 to 10
for i in range(1, 11):
    print("printing", i)


# Print all characters in a string
user_string = input("Enter a string: ")
for char in user_string:
    print(char)

# Print even numbers between 1 and 50
for num in range(1, 51):
    if num % 2 == 0:
        print(num)

# Categorize scores
scores = [85, 42, 78, 99, 65]
for score in scores:
    if score >= 60:
        print(f"{score}: Pass")
    else:
        print(f"{score}: Fail")

# Print your name 3 times
name = input("Enter your name: ")
for i in range(3):
    print(name)



