"""
 
2^x-2 <= a <= 2^x-1
 
x-2 <= log2(a) <= x-1
 
x-1 <= log2(a)+1 <= x
 
x <= log2(a)+2 <= x+1
 
 
1, 2, 4, 8, 16, 32
 
 
1 0 -2 -5 -9 -16 -24 -39
b       x = floor(log(b, 2))+1     plus
1       1                           1
2~3     2                           2 / 4
4~7     3                           4 / 8
8~15    4
16~31   5
 
2^(n-1) ~ 2^n - 1    n번
2^(n-1)<= b < 2^n
n-1 <= log2(b) < n
n <= log2(b)+1 < n+1    
-11? +16
-8? +8
-9? +16
-7? +8
 
log2(11) = 3.4
"""
from math import log2
import sys
input = sys.stdin.buffer.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    prev = a[0]
    for i in range(1, n):
        b = a[i]-prev
        if b >= 0:
            prev = a[i]
        else:
            x = int(log2(-b) + 1)
            res = max(res, x)
    print(res)