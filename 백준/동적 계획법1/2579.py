n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1] + stair[2])
else:
    result = [0]
    result.append(stair[1])
    result.append(stair[1]+stair[2])
    for i in range(3, n+1):
        result.append(max(result[i-3]+stair[i-1]+stair[i], result[i-2]+stair[i]))
    print(result[i])