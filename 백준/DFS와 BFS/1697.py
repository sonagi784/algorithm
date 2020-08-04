from collections import deque

def bfs(N, K):
    cnt = -1
    queue = deque()
    queue.append(N)
    visited = [False] * 100001
    visited[N] = True
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            now = queue.popleft()
            if now == K:
                return cnt
            if (now - 1) >= 0 and not visited[now - 1]:
                queue.append(now - 1)
                visited[now - 1] = True
            if (now + 1) <= 100000 and not visited[now + 1]:
                queue.append(now + 1)
                visited[now + 1] = True
            if (now * 2) <= 100000 and not visited[now * 2]:
                queue.append(now * 2)
                visited[now * 2] = True
    return cnt
    
N, K = map(int, input().split())
print(bfs(N, K))