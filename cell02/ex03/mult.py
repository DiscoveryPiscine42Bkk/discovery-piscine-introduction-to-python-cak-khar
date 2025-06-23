#!/usr/bin/env python3
print("enter the first number:")
first_number = input()
print("enter the second number:")
second_number = input()
product = int(first_number) * int(second_number)
print(first_number,"x",second_number,"=",product)
if int(product) == 0 :
    print("the result is zero")
if int(product) > 0 :
    print("the result is positive")
if int(product) < 0 :
    print("the result is negative")