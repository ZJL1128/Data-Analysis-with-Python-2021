#!/usr/bin/env python3

from re import S


def sum_equation(L):
    if not L:
        s = "0 = 0"
    else:

        s = " + ".join(str(i) for i in L)
        s += f" = {str(sum(L))}"
        
    

    return s

def main():
    pass
    print(sum_equation([1,5,7]))
if __name__ == "__main__":
    main()
