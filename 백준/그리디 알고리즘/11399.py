N = int(input())
P = list(map(int, input().split()))
P.sort(reverse=True)
result = 0
for i in range(0, len(P)):
    result += (P[i] * (i+1))
print(result)