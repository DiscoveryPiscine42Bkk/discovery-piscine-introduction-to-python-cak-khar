#!/usr/bin/env python3
str = input("what you gotta say? :")
if str != "STOP":
    while True:
        str = input("I got that! Anything else? :")
        if str == "STOP":
            break