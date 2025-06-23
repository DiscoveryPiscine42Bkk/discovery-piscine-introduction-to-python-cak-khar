#!/usr/bin/env python3
i = 0
while i <=10:
    print(f"table de {i}: ",end = " ")
    j = 0
    while j <= 10:
        print(i*j, end = " ")
        j +=1 #Increment num counter
    print()
    i +=1 #Increment num outer loop