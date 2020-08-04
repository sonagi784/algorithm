import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    if (n//2) % 2 != 0:
        print('NO')
    else:
        print('YES')
        res = 2
        for i in range(n//2):
            print(res, end=' ')
            res += 2
        res = 1
        for i in range(n//2-1):
            print(res, end=' ')
            res += 2
        print(res+n//2)