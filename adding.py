#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This program shows how global and local variables work


def main():
    # this function adds two integers together

    integer1 = int(input("Enter the first integer to be added "))
    integer2 = int(input("Enter the second integer to be added"))
    total = integer1 + integer2

    print("{0} + {1} = {2}".format(integer1, integer2, total))


if __name__ == "__main__":
    main()
