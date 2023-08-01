import os
import sys
import collections
import math

def nCr(n, r):
    res = 1

    #calculating nCr
    for i in range(r):
        res *= (n - i)
        res /= (i + 1)
    return int(res)

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    result = []
    for row in range(1, n+1):
        tempLst = []
        for col in range(row):
            tempLst.append(nCr(row-1, col))
        result.append(tempLst)
    return result

if __name__ == '__main__':
    n = 4
    result = printPascal(n)
    for i in result:
        for j in i:
            print(j, end=' ')
        print()