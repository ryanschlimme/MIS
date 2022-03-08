# Ryan Schlimme
# 07 March 2022

# This program takes a command line string with positive or negative numbers entered with one operation,
# either addition, subtraction, or multiplication, and computes the answer, given there are no spaces in the string.
# If an unexpected input is entered, it returns value "NA".

import string
import re
import sys


def split(delimiters, string, maxsplit=0):
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)


def isnumber(string):
    for s in string:
        if not s.isdigit():
            return False
    return True


delimeters = "+", "-", "*"
str = sys.argv[1]
equation = split(delimeters, str)
equation1 = list(filter(None, equation))

if not (isnumber(equation1[0]) and isnumber(equation1[1])):
    print("NA")
    exit()

if equation[0] == '':
    Num0 = int(equation[1])
    Num1 = (-1) * Num0
    Num2 = int(equation[2])
elif equation[1] == '':
    Num1 = int(equation[0])
    Num0 = int(equation[2])
    Num2 = (-1) * Num0
else:
    Num1 = int(equation[0])
    Num2 = int(equation[1])

if "+" in str:
    print(Num1 + Num2)
    exit()
elif "*" in str:
    print(Num1 * Num2)
elif "-" in str:
    print(Num1 - Num2)
    exit()
else:
    print("NA")
    exit()
