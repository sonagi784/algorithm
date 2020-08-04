import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    x, y, n = map(int, input().split())
    # k = 0~n k%x=y max(k)
    # k= x*z + y, z == k//x
 
    z = n // x
    if z*x + y > n:
        z -= 1
    print(z*x + y)