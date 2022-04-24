#!/usr/bin/env python3

import sys
#from sympy import continued_fraction


def extract_numbers(s):
    a = []
    x = s.split()
    for i in x:
        try:
            num = int(i)
            a.append(num)
        except ValueError:
            try:
                num = float(i)
                a.append(num)
            except ValueError:
                pass


    return a

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
