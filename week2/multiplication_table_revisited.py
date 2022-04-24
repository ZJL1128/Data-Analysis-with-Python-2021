#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a = np.arange(0,n)  #0到n equal a = np.arange(n)
    b = a.reshape((n,1))
    array = a * b


    return array

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
