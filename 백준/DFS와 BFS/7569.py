from collections import deque
import sys
input = sys.stdin.readline

def bfs(tomato, M, N, H):
    queue = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 1:
                    queue.append((h, n, m))
    dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    cnt = -1
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            for idx in range(6):
                nx, ny, nz = x + dx[idx], y + dy[idx], z + dz[idx]
                if (0 <= nx < H) and (0 <= ny < N) and (0 <= nz < M) and tomato[nx][ny][nz] == 0:
                    tomato[nx][ny][nz] = 1
                    queue.append((nx, ny, nz))
                
    for tom in tomato:
        for t in tom:
            if 0 in t:
                return -1
    return cnt

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
print(bfs(tomato, M, N, H)) # [H][N][M]