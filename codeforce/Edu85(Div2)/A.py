import sys
input = sys.stdin.readline
for _ in range(int(input())):
    CHECK = True
    p1, c1 = 0, 0
    n = int(input())
    for _ in range(n):
        p2, c2= map(int, input().split())
        if p2-p1 >= c2-c1 and c2-c1>=0:
            None
        else:
            CHECK = False
        p1, c1 = p2, c2
    print('YES' if CHECK else 'NO')     