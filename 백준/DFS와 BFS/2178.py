from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
miro = [list(map(int, list(input()))) for _ in range(N)]
q = deque()

q.append((0, 0))
while q:
    x, y = q.popleft()
    for i in range(4):
        n, m = x+dx[i], y+dy[i]
        if 0<=n<N and 0<=m<M and miro[n][m] == 1:
            miro[n][m] = miro[x][y] + 1
            q.append((n, m))

print(miro[-1][-1])