#!/usr/bin/env python3

def reverse_dictionary(d):
    newdict = {}
    for key,value in d.items():
        for val in value:
            newdict.setdefault(val,[]).append(key)
    
    
                    

    return newdict

    

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    pass
    

if __name__ == "__main__":
    main()
