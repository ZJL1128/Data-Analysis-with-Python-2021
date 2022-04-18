#!/usr/bin/env python3

def transform(s1, s2):
    s1 = map(int,s1.split())
    s2 = map(int,s2.split())
    
    S = [i*j for i,j in zip(s1,s2)]
    
    
    
    return S

def main():
    pass
    s1 =("1 5 3")
    s2 = ("2 6 -1")
    print(transform(s1,s2))

if __name__ == "__main__":
    main()
