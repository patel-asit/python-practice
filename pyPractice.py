# FROM THE WEBSITE https://www.w3resource.com/python-exercises/

#
#  Python Basic (Part -1) - Exercises, Practice, Solution
#

import datetime  # for PROBLEM 3
import sys  # for PROBLEM 2
import math  # for problem 4

problemNo = 1

print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

str = """Twinkle, twinkle, little star,
\tHow I wonder what you are!
\t\tUp above the world so high,
\t\tLike a diamond in the sky.
Twinkle, twinkle, little star,
\tHow I wonder what you are"""

print(str)

print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
# print(sys.__doc__)

print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

now = datetime.datetime.now()
print("Current date and time: {}".format(now))

# date.strftime(format) returns a string representing the date,
# controlled by an explicit format string.
# Format codes referring to hours, minutes or seconds will see 0 values.
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# NEED HELP IN THIS CODE

print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

# import math module at the top of this program

radius = float(input("Enter a radius: "))  # input is string, concatenate it

print("Area = {}".format(math.pow(radius, 2) * math.pi))


print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

full_name = input("Enter full name: ")

names = full_name.split()
if len(names) == 1:
    print("Your name in reverse is: {}".format(names[0]))
else:
    print("Your name in reverse is: {} {}".format(names[1], names[0]))


print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

string = input("Enter input: ").split(",")
tuples = tuple(string)
print(string)
print(tuples)

print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

color_list = ["Red", "Green", "White", "Black"]
print("{} {}".format(color_list[0], color_list[-1]))


print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

exam_st_date = (11, 12, 2014)
print("The examination will start from: %i/%i/%i" % exam_st_date)


print("{}================= {} =================".format("\n", problemNo))
problemNo += 1

n = input("Enter a number n:")
print(6*n)
