from heapq import heappush, heappop

def dijkstra(k):
    dp = [INF] * (N+1)
    dp[k] = 0
    heap = []
    heappush(heap, (0, k))
    while heap:
        w, v = heappop(heap)
        for wei, ver in graph[v]:
            if dp[ver] > w + wei:
                dp[ver] = w + wei
                heappush(heap, (w+wei, ver))

    return dp

INF = float('inf')
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) # heap은 weight가 먼저
    graph[b].append((c, a)) # 양방향 edge
v1, v2 = map(int, input().split()) # 1->v1->v2 -> N or 1->v2->v1->N
case1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]
case2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]

if case1 == case2 == INF:
    print(-1)
else:
    print(min(case1, case2))