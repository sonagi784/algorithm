N = int(input())
num = [[0] * 10 for _ in range(N)]
for i in range(1, 10):
    num[0][i] += 1
if N > 1:
    for i in range(len(num)-1):
        num[i+1][1] += num[i][0]
        num[i][0] = 0

        num[i+1][8] += num[i][9]
        num[i][9] = 0

        for j in range(1, 9):
            num[i+1][j-1] += num[i][j]
            num[i+1][j+1] += num[i][j]
            num[i][j] = 0


print(sum(num[-1])%1000000000)