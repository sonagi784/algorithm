import sys
input = sys.stdin.buffer.readline
N = int(input())
p = []
for i in range(N):  
    p.append(list(map(int, input().split())))
for i in range(1, N):
    p[i][0] += min(p[i-1][1], p[i-1][2])
    p[i][1] += min(p[i-1][0], p[i-1][2])
    p[i][2] += min(p[i-1][0], p[i-1][1])
print(min(p[-1]))