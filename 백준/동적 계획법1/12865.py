N, K = map(int, input().split())
weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1): # dp[i][j] : 갯수가 i개, 무게가 j일때 나올수있는 최대 벨류
        w, v = weights[i-1], values[i-1] # i번째 무게와 벨류
        if j < w: #지금 주어진 무게(j)로는 w 추가불가능
            dp[i][j] = dp[i-1][j]
        else: # w 추가가능 -> 추가할까 말까
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
print(dp[-1][-1])