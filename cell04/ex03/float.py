def classify_and_convert_number():
    user_input = input("Give me a number: ")
    try:
        num_float = float(user_input)
        if num_float.is_integer():
            num_int = int(num_float)
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print()
classify_and_convert_number()                    
