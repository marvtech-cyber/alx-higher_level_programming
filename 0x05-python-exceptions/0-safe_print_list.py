#!/usr/bin/python3
"""
function that prints x elements of a list
"""


def safe_print_list(my_list=[], x=0):
    length = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            length += 1
        except IndexError:
            break

    print()

    return (length)
