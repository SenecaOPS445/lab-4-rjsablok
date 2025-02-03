#!/usr/bin/env python3

# Strings 1
str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    # Returns the first five characters of the given string
    return string[:5]

def last_seven(string):
    # Returns the last seven characters of the given string
    return string[-7:]

def middle_number(number):
    # Returns the second and third characters of the number as a string
    return str(number)[1:3]

def first_three_last_three(string1, string2):
    # Returns a string that starts with the first three characters of string1 and ends with the last three characters of string2
    return string1[:3] + string2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
