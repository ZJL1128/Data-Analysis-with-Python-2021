#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    new_df = df[df["Air temperature (degC)"] < 0]
    num = len(new_df)
    return num

#suggested solution 
#return sum(df["Air temperature (degC)"] < 0.0)

def main():
    result = below_zero()
    print(f"Number of days below zero: {result}")
    return
    
if __name__ == "__main__":
    main()
