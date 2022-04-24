#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    #the numerator 
    prod = np.multiply(X,Y)
    dotProduct = np.sum(prod)

    #the norm
    normX = np.sqrt(np.sum(np.square(X)))
    normY = np.sqrt(np.sum(np.square(Y)))

    #the fraction
    fraction = dotProduct / (np.multiply(normX,normY))
    angle = np.arccos(fraction)

    return np.array(np.degrees(angle))

    

def main():
    X = np.array([[0,2]])
    Y = np.array([[3,3]])
    vector_angles(X, Y)

if __name__ == "__main__":
    main()
