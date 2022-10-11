import math
import os
import random
import re
import sys

def maxMin(k, arr):
    arr.sort()
    unfair = 100**100
    
    for i in range(len(arr)-k+1):
        if ((arr[i+(k-1)]-arr[i]) < unfair):
            unfair = arr[i+(k-1)]-arr[i]
        else:
            continue
    return unfair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()