#!/usr/bin/env python3
print("enter a number less than 25")
number_entered = int(input())
i = number_entered
if i <=25:
    while i<=25:
        print("inside the loop, my variable is",i)
        i +=1
else:
    print("Error")