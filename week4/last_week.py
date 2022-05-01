#!/usr/bin/env python3

import pandas as pd
import numpy as np
def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep = "\t")
    
    df.replace({"New":None,"Re": None},value = None,inplace = True)
    df = df.dropna()
    
    df = df.astype({'LW':int})
    
    #If peak postion is current potion, then replace with n/a
    mask = ((df['Peak Pos'] == df['Pos']) & (df['Pos']<df['LW']))
    df.loc[mask, 'Peak Pos'] = np.nan

    #decrease all counts of WoC by One
    df['WoC'] -= 1

    #Sort by Last Weeks chart rank
    df = df.astype({'LW':int})
    df_sorted = df.sort_values(by='LW')

    #reindex dataframe
    df_sorted.index = df_sorted['LW']
    df_sorted = df_sorted.reindex(range(1,41))

    #Replace Current Position with LW
    df_sorted['Pos'] = df_sorted.index

    #Replace LW with None
    df_sorted['LW'] = np.nan
    
    return df_sorted




    return pd.DataFrame()

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
