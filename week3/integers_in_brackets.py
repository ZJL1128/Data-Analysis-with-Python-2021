#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    mo = re.findall(r'\[\s*([+-]?\d+)\s*\]',s)
    mo = list(map(int,mo))
    return mo

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))
    pass

if __name__ == "__main__":
    main()
