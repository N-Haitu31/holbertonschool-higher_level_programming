#!/usr/bin/python3

def print_last_digit(number):

    abs = abs(number)
    last_dig = abs % 10

    print("{}".format(last_dig), end="")

    return last_dig
