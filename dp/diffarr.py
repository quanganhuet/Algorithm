#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def initializedDiffArray(A):
    n= len(A)

    D= [0 for i in range(0, n+1)]

    D[0] = A[0]
    D[n] = 0

    for i in range(1,n):
        D[i]= A[i] - A[i-1]
    return D

def update(D, l, r, x):
    D[l] += x 
    D[r+1] -= x

def printArray(A,D):
    for i in range(0, len(A)):
        if(i==0):
            A[i]= D[i]
        else:
            A[i]= D[i]+A[i-1]
              
def arrayManipulation(n, queries):
    A= [0] * n
    D = [0] * (n + 1)
    for i in range(len(queries)):
        update(D, queries[i][0]-1, queries[i][1]-1, queries[i][2])

    max_value = 0
    current_value = 0
    for i in range(n):
        current_value += D[i]
        if current_value > max_value:
            max_value = current_value
        
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
