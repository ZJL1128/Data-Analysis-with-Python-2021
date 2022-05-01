#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    values = s.values
    indices = s.index
    a = pd.Series(indices,index = values)

    return a

def main():
    s = pd.Series([1,2,3,4,5],index = list("abcde"))
    print(inverse_series(s))

if __name__ == "__main__":
    main()
