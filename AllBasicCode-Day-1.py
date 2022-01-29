#Program 1st
# print (2*9)
# print("Hello World")
# print("Hy Zeeshan!")

#program 2nd
# print(2+9)
# print(2-9)
# print(2*9)
# print(2/9)
# print(2**9)
# print(2//9)
# print(2%9)
# print(2**0.5)
# print(2**0.25)
# #PEMDAS
# print(2+9*9/9-9)
# print(2**9//9%9)

# program 3rd
# String
# print("Hello World")
# print("Hello"+"Zeeshan")
# print("Hello"*3)
# print("Hello"+"World"*3)
# print("Hello"*3+"World")
# print("Hello"*3+"World"*3)
# print("Hello"*3+"World"*3+"!")


#program 4th
#Comment In Python
# Commenting is done using #
# Commenting is done using """ """
# Ctrl + /

# program 5th
# Variables in Python
# x = 10
# y = 20
# z = x+y
# print(z)

# #type of variable
# print(type(x))
# print(type(y))

# #Rules to assign variable
# #1. Variable name must start with a letter or an underscore
# #2. Variable name is case sensitive
# #3. Variable name should not be a Python keyword
# #4. Variable name should be meaningful and descriptive

# fruit = ('Apple',"Orange","Banana")
# print(type(fruit))
# print(fruit)

# program 6th
#  Input in Python
# input Function
# fruit_basket =input("What is your Favourite ? ")
# print(fruit_basket)

# input Function with 2nd stage
# name = input("What is your name ? ")
# greeting = "Hello"
# print(greeting, name)

# another way to input
# name = input("What is your name ? ")
# print("Hello", name)

# another way to input
# name = input("What is your name ? ")
# age = input("What is your age ? ")
# greeting = "Hello"
# print(greeting, name, "you are", age)

#Program 7th
# Condition Logical Operation in Python
# equal to ==
# not equal to !=
# greater than >
# less than <
# greater than or equal to >=
# less than or equal to <=
# and
# or
# not
# print(1==1)
# print(1==2)
# print(1!=2)
# print(1>2)
# print(1<2)
# print(1>=2)
# print(1<=2)
# print(1==1 and 2==2)
# print(1==1 or 2==2)
# print(not(1==1))
# print(not(1==2))

# Application of Logical Operator
# imtanan = 4
# age_at_school = 5
# print(imtanan==age_at_school)

#input and Logical Operator
# age_at_school = 5
# imtanan = int(input("What is your age ? ")) #input function
# print(imtanan==age_at_school) #Logical Operator

#Program 8th
#Type Conversion in Python
# int()
# float()
# str()
# bool()
# x = 10   #int
# y = 20.5  #float
# z = "Hello" #string
# #implicit type conversion
# x = x*y
# print(type(x))

# explicit type conversion
# age = float(input("What is your age ? "))
# print(type(age))

# Program 9th
# IF Else Elsif Else in Python
# if condition:
# age_at_school = 5
# imtanan = 6
# # if condition:
# if imtanan==age_at_school:
#     print("You are in school")
# elif imtanan>age_at_school:
#     print("Cong! You are in school")
# else:
#     print("You are not in school")

# Program 10th
# Functions in Python
# def function_name(parameter):
# def print_shani():
#     text ="I love my brother"
#     print(text)
#     print(text)
#     print(text)
  
# print_shani()

# #2nd way to write function
# def print_shani_2(text):
#     print(text)
#     print(text)
#     print(text)
# print_shani_2("I love my brother")

# #3rd way to write function
# def print_shani_3(text):
#     print(text)
#     print(text)
#     print(text)
#     print_shani_3("I love my brother")

#Program 11th
# defining a function with if else function
# def  school_calculator(age_at_school,imtanan):
#     if imtanan==age_at_school:
#         print("You are in school")
#     elif imtanan>age_at_school:
#         print("Cong! You are in school")
#     else:
#         print("You are not in school")
# school_calculator(4,2)


# Defining a function of Future
# def future_age(age,year):
#     new_age= age+20
#     return new_age

# future_prediction = future_age(14,2020)
# print(future_prediction)

# Program 12th
# Loop in Python
# for loop
# for i in range(150):
#     print(i)

#while loop
# i=0
# while i<10:
#     print(i)
#     i=i+1

# Array in Python
# fruits = ["Apple","Orange","Banana"]
# for fruit in fruits:
#     print(fruit)

#Program 13th

# import Library in Python
# import math
# import statistics
# print(math.sqrt(16))
# print(math.pi)
# print(math.sin(math.pi/2))


# x=(150,250,350,450,550)
# print(statistics.mean(x))
# print(statistics.median(x))
# print(statistics.mode(x))
# print(statistics.variance(x))
# print(statistics.stdev(x))

#program 14th
# Troubleshooting in Python
# print(we are learning paython) #SyntaxError: invalid syntax
# print("we are learning paython") #SyntaxError: invalid syntax
# print(25/0) #ZeroDivisionError: division by 
# name = "Zeeshan"
# print("Hello name"  + name)

# information about error
# print(name)


# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

# Print out house
print(house)

# Subsetting Lists
# 1. Subsetting Lists
# After you've created your very own Python list, you'll need to know how you can access information in the list.

# 2. Subsetting lists
# Python uses the index to do this. Have a look at the fam list again here. The first element in the list has index 0, the second element has index 1, and so on. Suppose that you want to select the height of emma, the float 1-point-68. It's the fourth element, so it has index 3. To select it, you use 3 inside square brackets. Similarly, to select the string "dad" from the list,

# 3. Subsetting lists
# which is the seventh element in the list, you'll need to put the index 6 inside square brackets. You can also count backwards, using negative indexes. This is useful if you want to get some elements at the end of your list. To get your dad's height, for example, you'll need the index -1. These are the negative indexes for all list elements.

# 4. Subsetting lists
# This means that both these lines return the exact same result. Apart from indexing, there's also something called slicing,

# 5. List slicing
# which allows you to select multiple elements from a list, thus creating a new list. You can do this by specifying a range, using a colon. Let's first have another look at the list, and then try this piece of code. Can you guess what it'll return? A list with the the float 1-point-68, the string "mom", and the float 1-point-71, corresponding to the 4th, 5th and 6th element in the list maybe? Let's see what the output is. Apparently, only the elements with index 3 and 4, get returned. The element with index 5 is not included. In general, this is the syntax: the index you specify before the colon, so where the slice starts, is included, while the index you specify after the colon, where the slice ends, is not. With this in mind, can you tell what this call will return? You probably guessed correctly that this call gives you a list with three elements, corresponding to the elements with index 1, 2 and 3 of the fam list. You can also choose to just leave out the index before or after the colon.

# 6. List slicing
# If you leave out the index where the slice should begin, you're telling Python to start the slice from index 0, like this example. If you leave out the index where the slice should end, you include all elements up to and including the last element in the list, like here. Now it's time to head over to the exercises,

# 7. Let's practice!
# where you will continue to work on the list you've created yourself before. You'll use different subsetting methods to get exactly the piece of information you need!

# Create the areas list
#areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# # Use slicing to create downstairs
# print(areas[:6])
# # Use slicing to create upstairs
# print(areas[4:])
# Slicing and dicing (2)
# In this exercise, you will be working with the list areas, which contains the area of different rooms in a house. The list has been pre-loaded for you.
# Alternative slicing to create upstairs
 