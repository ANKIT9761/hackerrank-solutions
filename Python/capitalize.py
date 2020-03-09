#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    count=0
    t=''
    for i in s:
        if(i==' '):
            t=t+' '
            count=0
        else:

            if(count==0):
                t=t+i.capitalize()
                count=count+1
        
            else:
                t=t+i
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
