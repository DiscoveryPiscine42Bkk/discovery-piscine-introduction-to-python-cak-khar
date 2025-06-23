#!/usr/bin/env python3
print("Enter a number:")
number_in = int(input())
num = 0
i = num
if i <12:
    while i<12:
        i +=1
        result = int(i)*int(number_in)
        print(i,"x",number_in,"=",result)