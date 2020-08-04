def dfs(adj, start):
    stack = [start]
    visit = []
    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            for idx in range(1, N+1):
                if adj[n][idx] == 1 and idx not in visit:
                    stack.append(idx)
    return visit

N = int(input())
V = int(input())
adj = [[0] * (N+1) for _ in range(N+1)]
for _ in range(V):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1
print(len(dfs(adj, 1)) - 1)