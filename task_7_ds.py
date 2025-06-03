# *************************************_____TASK_6*************************************************************

# Function with Default Argument
def greet(name, message="Welcome!"):
    print(f"Hello, {name}! {message}")

# Call with default message
greet("Nabin")

# Call with custom message
greet("Nabin", "Good to see you!")


# Function with args (Variable Number of Arguments)
def total(*numbers):
    print("Sum of numbers:", sum(numbers))

# Example call
total(5, 10, 15)

    

# Function using **kwargs (keyword arguments):

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Rajesh", age=25, city="Kathmandu")    



# Function Using Both args and a Default Argument
def repeat_words(*words, times=2):
    for word in words:
        print(word * times)

repeat_words("Hi", "Bye", times=3)


# Function Using All Types of Parameters Together
def user_profile(name, age=18, *hobbies, **extra_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("No hobbies provided.")
        
    if extra_info:
        print("Additional Info:")
        for key, value in extra_info.items():
            print(f"{key}: {value}")
    else:
        print("No additional info provided.")

user_profile("Rajesh", 25, "Reading", "Cycling", city="Kathmandu", profession="Engineer")
