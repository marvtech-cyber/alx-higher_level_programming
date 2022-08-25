#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    for nb_arg in range(1, len(sys.argv)):
        sum += int(sys.argv[nb_arg])
    print(sum)
