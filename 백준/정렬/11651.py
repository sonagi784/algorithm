N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    temp = []
    temp.append(y)
    temp.append(x)
    arr.append(temp)
arr.sort()
for i in range(N):
    y, x = arr[i]
    print(x, y)