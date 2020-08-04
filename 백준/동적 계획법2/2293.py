N, K = map(int, input().split())
coin =[0] + sorted([int(input()) for _ in range(N)])
dp = [0] * (K+1)
for i in range(coin[1], K+1, coin[1]):
    dp[i] = 1
dp[0] = 1

for c in coin[2:]:
    for k in range(1, K+1):
        if c <= k:
            dp[k] = dp[k] + dp[k-c]

print(dp[-1])