#!/usr/bin/env python3

import pandas as pd
from os import sep

def main():
    df = pd.read_csv("src/municipal.tsv", sep='\t')
    shape = df.shape
    print(f"Shape: {shape[0]},{shape[1]}")
    print("Columns:")
    for x in df.columns:
        print(x)

    return


if __name__ == "__main__":
    main()
