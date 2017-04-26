"""
Patrick Danford 
Lab 4, Reverse integer

Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321

"""

number = input("Enter a 3 number at least 3 digits: ")

reverse = 0
while number > 0:
    remainder = number % 10
    reverse = (reverse * 10) + remainder
    number = number / 10

print reverse