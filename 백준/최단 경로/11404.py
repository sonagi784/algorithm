n = int(input())
m = int(input())
INF = float('inf')
bus = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
                if i != j:
                    bus[i][j] = min(bus[i][j], bus[i][k]+bus[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(0 if bus[i][j] == INF else bus[i][j], end=' ')
    print()
