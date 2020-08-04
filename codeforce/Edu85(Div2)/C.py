import sys
input = sys.stdin.buffer.readline
 
for _ in range(int(input())):
    n = int(input())
    a, b, c = [], [], []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
 
    for i in range(n):
        c.append(max(a[i] - b[i-1], 0))
 
    for i in range(n):
        a[i] -= c[i]
    
    print(sum(c)+min(a))