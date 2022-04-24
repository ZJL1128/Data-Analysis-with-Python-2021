#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    res = []
    with open(filename,'r') as f:
        for l in f:
            temp=re.findall(r'\S+\s\d\s\w+\s\S+\s+(\d+)\s([a-zA-Z]{3})\s+(\d{1,})\s(\d+):(\d+)\s(.+)',l)
            temp = (int(temp[0][0]), temp[0][1], int(temp[0][2]), int(temp[0][3]), int(temp[0][4]), temp[0][5])
            res.append(temp)


    return res 
def main():
    print(file_listing())
    

if __name__ == "__main__":
    main()
