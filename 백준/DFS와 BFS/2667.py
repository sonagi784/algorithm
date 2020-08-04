def dfs(home, a, b):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 1
    stack = [(a ,b)]
    home[a][b] = 0
    while stack:
        a, b = stack.pop()
        for (dx, dy) in d:
            x, y = a + dx, b + dy
            if 0 <= x and x < N and 0 <= y and y < N and home[x][y] == 1:
                cnt += dfs(home, x, y)
    return cnt

N = int(input())
home = [list(map(int, list(input()))) for _ in range(N)]
aptcomplex = 0
res = []
for a in range(N):
    for b in range(N):
        if home[a][b] == 1:
            aptcomplex += 1
            res.append(dfs(home, a, b))
print(aptcomplex)
for i in sorted(res):
    print(i)