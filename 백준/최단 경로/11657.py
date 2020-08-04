def Bellman(s):
    d = [INF] * (N+1)
    d[s] = 0
    check = False
    for i in range(1, N+1): # (노드갯수-1)번 반복하면 음수 가중치까지반영됨
        for start in range(1, N+1): # 가중치 update) 모든 edge에 대해서 update
            for end, weight in graph[start]:
                if d[start] != INF and d[end] > d[start] + weight:
                    d[end] = d[start] + weight
                    if i == N: 
                        # (노드갯수)번째에서도 값이 변하고있다면 음의 사이클 무한반복중인것
                        check = True
    
    if check:
        return [-1]
    for i in range(2, N+1):
        if d[i] == INF:
            d[i] = -1
    return d[2:]

INF = float('inf')
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
for res in Bellman(1):
    print(res)
