#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    new_df1 = df["Population change from the previous year, %"]
    num1= len(new_df1)
    new_df2 = df[df["Population change from the previous year, %"] > 0]
    num2 = len(new_df2)
    dec = (num2/num1) 


    return dec

def main():
    df = pd.read_csv("src/municipal.tsv",sep = "\t",index_col = 0)
    df = df["Akaa":"Äänekoski"]
    dec = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {dec:.1f}%")

if __name__ == "__main__":
    main()
