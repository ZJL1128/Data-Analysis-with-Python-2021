#!/usr/bin/env python3

def merge(L1, L2):
    l2 = []
    l = L1 + L2
    while(l):
        temp = min(l)
        l2.append(temp)
        l.pop(l.index(temp))
    return l2

    
    

def main():
    pass
    L1=[1,4,6]
    L2=[3,5,9]
    L = merge(L1,L2)
    print(L)

if __name__ == "__main__":
    main()
