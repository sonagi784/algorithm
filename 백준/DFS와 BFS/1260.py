def dfs(graph, start):
    stack = [start]
    visit = []
    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            stack += sorted(list(graph[n] - set(visit)), reverse = True)
    return visit

def bfs(graph, start):
    queue = [start]
    visit = []
    while queue:
        n = queue.pop(0)
        if n not in visit:
            visit.append(n)
            queue += sorted(list(graph[n] - set(visit)), reverse = False)
    return visit

N, M, V = map(int, input().split())
graph = [set([]) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].add(j)
    graph[j].add(i)
print(*dfs(graph, V))
print(*bfs(graph, V))