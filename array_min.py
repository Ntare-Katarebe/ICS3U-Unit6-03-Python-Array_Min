#!/usr/bin/env python3

# Created by: Ntare-Katarebe
# Created on: June 2021
# This program uses an array(list) to find the largest number


import math
import random

my_numbers = []


def min_number(my_numbers):
    min = my_numbers[0]

    for loop_counter in my_numbers:
        if loop_counter < min:
            min = loop_counter

    return min


def main():
    # this function uses an array

    # input
    for loop_counter in range(0, 10):
        a_single_number = random.randint(1, 100)
        my_numbers.append(a_single_number)
        print("The random is: {0}".
              format(my_numbers[loop_counter]), end="\n")
    print("")

    print("The smallest number is {}".format(min_number(my_numbers)))
    print("\nDone.")


if __name__ == "__main__":
    main()
