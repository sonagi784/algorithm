N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
for i in range(N):
    x, y = arr[i]
    print(x, y)