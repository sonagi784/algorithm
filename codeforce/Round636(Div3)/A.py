import math
import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    for k in range(2, 30):
        x = n / (2**k - 1)
        if x == math.ceil(x):
            print(int(x))
            break