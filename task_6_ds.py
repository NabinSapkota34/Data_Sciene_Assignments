# *************************************_____TASK_6*************************************************************



# Print Numbers from 10 to 30
num = 10
while num <= 30:
    print("Number from 10 to 30 each are:", num)
    num += 1


# Print Odd Numbers from 1 to 20
num1 = 1

while num1 <= 20:
    if num1 % 2 != 0:
        print("Odd number from 1 to 20 is:", num1)
    num1 += 1

# Print a Word 5 Times
num3 = 1
word = "Hello"

while num3 <= 5:
    print(word)
    num3 += 1


# Countdown from 5
num2 = 5

while num2 >= 1:
    print(num2)
    num2 -= 1


# Print All Multiples of 3 up to 30
num4 = 1

while num4 <= 30:
    if num4 % 3 == 0:
        print("Multiple of 3:", num4)
    num4 += 1



# Keep Asking for a Number Until It's Positive
numin = int(input("Enter a positive number: "))

while numin <= 0:
    print("That’s not positive. Try again.")
    numin = int(input("Enter a positive number: "))

print("You are good:", numin)


# Print Even Numbers Between 10 and 20
num5 = 10
while num5 <= 20:
    if num5 % 2 == 0:
        print("Even number between 10 and 20 is:", num5)
    num5 += 1


# Guess the Secret Number using while loop
numsec = int(input("Enter a secret number: "))

while numsec != 7:
    print("That’s not secret. Try again.")
    numsec = int(input("Enter a secret number: "))

print("You are good:", numsec)


# Function to Add Two Numbers
def add(a, b):
    print(f"Addition is {a + b}")

add(5, 4)


# Function to Multiply Two Numbers
def mul(a, b):
    print(f"Addition is {a * b}")

mul(5, 4)



# Function to Check Even or Odd
def check_even(num6):
    if num6 % 2 == 0:
        print(f"Number is Even: {num6}")
    else:
        print(f"Number is Odd: {num6}")

check_even(12)
check_even(7)
