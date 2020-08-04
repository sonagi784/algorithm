from heapq import heappush, heappop

def dijkstra(k):
    dp = [INF] * (V+1)
    dp[k] = 0
    heap = []
    heappush(heap, (0, k)) # heap은 weight가 먼저 들어가게
    while heap: 
        w, n = heappop(heap) # k에 연결된 간선중 최단거리(k->n)
        for ver, wei in graph[n]: # n에 연결된 간선들(n->ver), graph는 ver, wei순서로
            if dp[ver] > w + wei: # k->ver(기존) vs k->n->ver(새로운)
                dp[ver] = w + wei # k->ver값 기존->새로운 수정
                heappush(heap, (w+wei, ver))
    
    return dp

V, E = map(int, input().split())
k = int(input())
INF = float('inf')
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

for res in dijkstra(k)[1:]:
    print(res if res != INF else 'INF')
    