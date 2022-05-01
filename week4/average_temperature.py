#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    new_df = df[df.m == 7]
    temp = new_df["Air temperature (degC)"]
    return temp.mean()

def main():
    result = average_temperature()
    print(f"Average temperature in July: {result:.1f}")
    return

if __name__ == "__main__":
    main()
