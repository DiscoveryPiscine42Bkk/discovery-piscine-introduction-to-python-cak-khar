print("enter a number less than 25")
number_entered = int(input())
i = number_entered
if i <25:
    while i<25:
        i +=1
        print("inside the loop, my variable is",i)
else:
    print("inside the loop, my variable is 25")