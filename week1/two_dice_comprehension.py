#!/usr/bin/env python3

def main():
    pass
    G= [(i,j) for i in range(1,7)
              for j in range(1,7)
              if i+j == 5]
    for i in G:
        print(i)

if __name__ == "__main__":
    main()
