#!/usr/bin/env python3
original_num = [2, 8, 9, 48, 8, 22, -12, 2]
filtered_num = []
for x in original_num:
    if x >= 5:
        filtered_num.append(x+2)
print(original_num)
print(filtered_num)