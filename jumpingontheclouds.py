#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    counter = 0
    
    while counter < len(c) - 1:
        if counter + 2 < len(c) and c[counter] == 0 and c[counter + 1] == 0 and c[counter + 2] == 0:
            jumps += 1
            counter += 2
        elif counter + 1 < len(c) and c[counter + 1] == 1:
            jumps += 1
            counter += 2
        else:
            jumps += 1
            counter += 1
        print(counter, jumps)
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
