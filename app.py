# VSCODE SHORTCUTS
# Ctrl Shift P for command pallete (aka basic search button)
# Ctrl Alt N for running code (note: gotta save the file first)
# Ctrl ~ to toggle built in terminal
# Ctrl Shift M for Problems tab
#

#
#   PYTHON BEGINNER ROADMAP (plans subject to change)
#   - finish YT video first https://www.youtube.com/watch?v=f79MRyMsjrQ&ab_channel=ProgrammingwithMosh
#   - then do PyPractice from bookmark
#   - then maybe do leetcode problems with this
#   - then maybe make small programs/projects using python
#

# if you specify int then mypy linter will complain if you change type
# but it still wont stop you, strange ey
students_count: int = 1000

students_count = "changed"
print(type(students_count))  # shows how types can change in python

rating = 4.99
is_published = False

course_name = """
Python supports
multiple lines
"""
x, y, z = 1, 2, "this one's string"  # see how we can declare multiple variables
x = y = 1

print(id(x))
x = 3  # ints are immutable, meaning its unchangeable so changes of int will be in a new location
print(id(x))

# but lists are mutable, check its location upon changing
x = [1, 2, 3, "string"]
print(id(x))
x.append(4)
print(id(x))

# =============== STRING LECTURES NOW ===============

course = "Python Programming"
print(len(course))  # len isnt specific for strings like .length() is in java.
# instead its generic reusable function. Python seems to be much versatile
# pass in string, it returns #of chars in string, pass it a list it returns its size

# see how we can simply access the string characters, we dont need to do "".charAt() as java
print(course[0])

# -ve index in python doesnt give error, it instead returns the end,
# -1 means last, -2 means second last character. Very powerful
print(course[-1])

# "slicing" a string, its like substring in java. prints 0..n-1 locations
print(course[0:3])
print(course[:3])  # so what will happen? it will auto insert start index 0
print(course[0:])  # how about now? it will auto insert string.length at end
print(course[:])  # now? it prints entire string

# ok remember how strings and other primitive types are immutable, so slicing doesnt
# affect the original string, it creates a new copy of the string
print(id(course))
print(id(course[0:3]))  # notice a new location, means its a new copy in memory
print(id(course[:]))  # see how  [:] doesnt create a new slice copy of string

# =============== ESCAPE SEQUENCES ===============
# Escape from string to make something work, escape seq. are activated by \

# \" puts double quotes in strings
# \' puts single quote in strings
# \\ puts backslash \ in strings
# \n puts new line in strings

# if we want to add double quote " within a string how to do it
message = 'Python "Programming'  # one way is to use single quotes at the end
message = "Python \"Programming"  # alternatively \" puts quotes in strings

# NOTE - imagine you have complex string to write with multiple lines, instead of using
# \n numerous times just use triple quotes and type a string as shown previously in this code

# =============== STRING FORMAT ===============

first = "Asit"
last = "Patel"
full = first + " " + last
print(full)

# above was a primitive way, below is new way with string formatting
first = "Asit"
last = "Patel"
full = f"{first} {last}"  # another way to do same concatenation
# f or F can be written in beginning
# NOTE - you can write anything in curly brackets, like {len(first)}
# and that will concatenate the number with last name
print(full)

# string format works like this
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print("\n{}".format(txt1))

# =============== USEFUL STRING METHODS ===============

course = "  String methods"
print(course.upper())
print(course.lower())
print(course.title())  # makes string sentence case, uppers each word first letter

print(course.strip())  # removes extra white-spaces, like trim() in java
# ALSO SEE: .lstrip() and .rstrip() these removes spaces from left or right

print(course.find("meth"))  # .find() returns the location of found item
print(course.find("Meth"))  # note this result, finding is case sensitive

print(course.replace("St", "Foste"))  # just like java replace() but no regex
# ASK SOMEONE WHETHER YOU COULD USE REGEX IN .replace() like you could in java meaning
# if you want to swap all numbers or all non-letter chars how to do it

# to check existence of a character or sequence of chars in string we use 'in' operator
# 'in' is an operator and 'not' is an operator so we can combine 'not in' also
print("String" in course)  # there is 'in' operator in python!! *~*
print("String" not in course)  # hover mouse on 'in' 'not' to read description


# =============== NUMBERS ===============

x = 10  # in python we can enter decimal numbers
x = 0b10  # and we can add binary numbers, but this is stored as decimal

print(x)  # print() always prints decimal value
print(bin(x))  # bin() returns binary representation of any number

x = 0x12c  # again we can use hex notation but stores as decimal
print(hex(x))  # prints in hex representations

# python also has support for complex numbers ie. a + bi
# we see how to represent those complex numbers
x = 1 + 2j  # j in python is like imaginary in math, we can write either J or j
print(x)

# =============== ARITHMETIC OPERATORS ===============

# we all necessary operators for arithmetic in python ie + - *
# but notably we have a few special ones

x = 10 / 3  # this way we get floating point exact answer
print(x)
x = 10 // 3  # this is how we do integer division
print(x)

x = 10 % 3  # ofcourse the modulus operator

x = 10 ** 3  # this is exponent operator, this is left^right = 10^3
print(x)

# Note: we dont have increment/decrement operators like x++/x--
# instead there are 'Augmented assignment operators' ie += *= -=

# =============== USEFUL FUNCTIONS FOR NUMBERS ===============

# in python since we dont have private final type, we have to
# resort to naming conventions instead, so uppercase variables
# tell the devs that it is a constant and shouldn't be changed
PI = -3.14

print(round(PI))  # rounds the number
print(abs(PI))  # returns abs value of input
print(abs(round(PI)))  # have fun lmao

# Note - for a full list of built-in functions, google Python 3 built-in functions

# if we want to perform more complex mathem. functions we have to import Math module
# that module is an Object
