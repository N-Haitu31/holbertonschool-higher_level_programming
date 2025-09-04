#!/usr/bin/python3
def print_last_digit(number):
    absolu = abs(number)
    last_dig = absolu % 10
    print("{}".format(last_dig), end="")
    return last_dig
