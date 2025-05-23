# Python Data Structures Assignment

# 1. Creating a List

a = ['abc', 123, True, 32.99, complex(32, 1)]
print(type(a[4])) 

# 2. List of Strings
fruits = ['apple','banana','guava','mango','pear']
print(fruits)

# 3.Accessing Elements
num = [10,20,30,40,50]
print(num[0],num[-1])

# 4.List Length
fruits = ['apple', 'banana', 'guava', 'mango', 'pear']
print(len(fruits), len(fruits[0]))


# 5.Appending Elements
b = []
b.append([1, 2])
print(b)



# 6. Inserting an Element
lst = [1, 3, 4]            
lst.insert(1, 2)           
print(lst)


# 7. Removing an Element
num2 = [1, 2, 3, 4, 5]
num2.remove(3)
print(num2)

# 8.Pop last element
num3 = [10, 20, 30, 40, 50]
last_element = num3.pop(-1)
print("Popped element:", last_element)
print("List after popping:", num3)

# 9.Slicing a List
num4 = [0,1,2,3,4,5]
print(num4[2:5])

# 12. List Concatenation
num6= [1,2,3]
num7 = [4,5,6]
result= num6 + num7;
print(result)

# 11. Repating a list 
num5 = [1, 2]
repeated_list = num5 * 2
print(repeated_list)

# 12. Copying a list 
original_list = [1, 2, 3]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)


# 13.Clearing a List 
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)








# Tuples

# 1. Create a Tuple
tuple1 = (1, 2, 3)
print("1. Tuple:", tuple1)

# 2. Tuple of Strings
colors = ("red", "green", "blue")
print("2. Colors tuple:", colors)

# 3. Accessing Tuple Elements
tuple2 = (10, 20, 30, 40)
print("3. Second element:", tuple2[1])  

# 4. Tuple Slicing
tuple3 = (0, 1, 2, 3, 4)
print("4. Slice from index 1 to 3:", tuple3[1:4])  

# 5. Concatenating Tuples
tuple4 = (1, 2)
tuple5 = (3, 4)
concatenated = tuple4 + tuple5
print("5. Concatenated tuple:", concatenated)

# 6. Tuple Unpacking
person = ("Alice", 25, "New York")
name, age, city = person
print("6. Unpacked values:")
print("Name:", name)
print("Age:", age)
print("City:", city)

# 7. Convert List to Tuple
list1 = [1, 2, 3, 4]
tuple_from_list = tuple(list1)
print("7. Tuple from list:", tuple_from_list)

# 8. Counting Occurrences
tuple6 = (1, 2, 2, 3, 2)
count_2 = tuple6.count(2)
print("8. Number of times 2 appears:", count_2)

# 9. Finding an Index
tuple7 = (10, 20, 30, 40)
index_30 = tuple7.index(30)
print("9. Index of element 30:", index_30)








