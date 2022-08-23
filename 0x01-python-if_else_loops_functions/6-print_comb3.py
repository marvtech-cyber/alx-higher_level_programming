#!/usr/bin/python3
for number1 in range(0, 8):
    for number2 in range(1, 10):
        if number1 != number2 and number2 > number1:
            print("{}{}, ".format(number1, number2), end="")
print(89)
