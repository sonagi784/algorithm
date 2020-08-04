n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))
dp = [0, wine[1]]
if n > 1:
    dp.append(wine[1]+wine[2])
    for i in range(3, n+1):
        case1 = dp[i-3] + wine[i-1] + wine[i]
        case2 = dp[i-2] + wine[i]
        case3 = dp[i-1]
        dp.append(max(case1, case2, case3))
print(dp[n])