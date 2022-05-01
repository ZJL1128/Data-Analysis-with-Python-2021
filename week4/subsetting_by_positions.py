#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep = "\t")
    #col = df.columns
    #subset = df.iloc[0:10][[col[1],col[2]]]
    #return pd.DataFrame(subset) 
    return df.iloc[:10,2:4] #Suggested solution

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()
