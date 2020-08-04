N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort(reverse=True)
result = 0

for a in A:
    if K >= a:
        coin = K // a
        K -= a * coin
        result += coin

print(result)