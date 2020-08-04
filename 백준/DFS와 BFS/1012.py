def bfs(cabbage, i, j):
    queue = [(i, j)]
    cabbage[i][j] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.pop(0)
        for idx in range(4):
            m, n = x + dx[idx], y + dy[idx]
            if 0 <= m and m < M and 0 <= n and n < N and cabbage[m][n] == 1:
                queue.append((m, n))
                cabbage[m][n] = 0
    
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    cnt = 0
    cabbage = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[x][y] = 1
    for i in range(M):
        for j in range(N):
            if cabbage[i][j] == 1:
                bfs(cabbage, i, j)
                cnt += 1
    print(cnt)