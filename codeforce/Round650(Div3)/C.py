import sys, math
input = sys.stdin.readline
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().rstrip()))
    if 1 not in s:
        print(math.ceil(n/(k+1)))
        continue
 
    for i in range(n):
        if s[i] == 1:
            left = max(0, i-k)
            right = min(i+k, n-1)
            for j in range(left, right+1):
                s[j] = -1
    result = 0
    for i in range(n):
        if s[i] == 0:
            result += 1
            left = max(0, i-k)
            right = min(i+k, n-1)
            for j in range(left, right+1):
                s[j] = -1
    print(result)