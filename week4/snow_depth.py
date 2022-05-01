#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    #df_des = df.describe()
    #return df_des.loc["max"]["Snow depth (cm)"]
    return df["Snow depth (cm)"].max() # suggested solotion

def main():
    
    print(f"Max snow depth: {snow_depth()}")
    return

if __name__ == "__main__":
    main()
