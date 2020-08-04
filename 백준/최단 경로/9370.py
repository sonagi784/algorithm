from heapq import heappush, heappop
INF = float('inf')

def dijkstra(start):
    dp = [INF] * (n+1)
    dp[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        w, v = heappop(heap)
        for wei, ver in graph[v]:
            if dp[ver] > w+wei:
                dp[ver] = w+wei
                heappush(heap, (w+wei, ver))
    
    return dp

for _ in range(int(input())):
    n, m, T = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    des = []
    for _ in range(T):
        des.append(int(input()))
    
    for tmp in graph[g]:
        if h == tmp[1]:
            smell = tmp[0]
    c1 = dijkstra(s)[g] + smell
    c2 = dijkstra(s)[h] + smell
    res = []
    for t in des:
        case1 = c1 + dijkstra(h)[t]
        case2 = c2 + dijkstra(g)[t]
        destination = dijkstra(s)[t]
        if case1 + case2 + destination == INF: # 경로가 없는 경우
            continue;

        if case1 == destination or case2 == destination:
            res.append(t)

    print(*list(sorted(res)))