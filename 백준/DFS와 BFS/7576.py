def bfs(tomato, M, N):
    from collections import deque
    ripe = deque()
    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 1:
                ripe.append((n, m))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = -1
    while ripe: # max : O(N^2)
        cnt += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft() # pop() : O(1), pop(n) : O(N)
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if (0 <= nx < N) and (0 <= ny < M) and tomato[nx][ny] == 0:
                    tomato[nx][ny] = 1
                    ripe.append((nx, ny))
                    
    for t in tomato:
        if 0 in t:
            return -1
    return cnt
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
print(bfs(tomato, M, N))