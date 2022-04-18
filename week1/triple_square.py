#!/usr/bin/env python3

def triple(a):
    return a*3

def square(b):
    return b**2

def main():
    pass
    for i in range(1,11):
        s = triple(i)
        t = square(i)
        if(t > s):
                break
        print(f"triple({i})=={i*3}",end = " ")
        print(f"square({i})=={i**2}")
        



if __name__ == "__main__":
    main()
