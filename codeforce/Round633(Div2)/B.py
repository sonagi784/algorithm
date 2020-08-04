import sys
input = sys.stdin.buffer.readline
 
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    idx = n // 2
    sign = 1
    for i in range(n):
        print(a[idx], end=' ')
        idx -= sign * (i+1)
        sign *= -1
    print()