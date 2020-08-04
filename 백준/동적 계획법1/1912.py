n = int(input())
a = list(map(int, input().split()))
dp = [a[0]]
for i in range(1, n):
    dp.append(max(dp[i-1]+a[i], a[i]))
print(max(dp))