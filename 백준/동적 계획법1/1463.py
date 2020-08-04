arr = [0, 0] + [1e7] * 3000000
for i in range(1, int(1e6+1)):
    arr[i+1] = min(arr[i+1], arr[i]+1)
    arr[i*2] = min(arr[i*2], arr[i]+1)
    arr[i*3] = min(arr[i*3], arr[i]+1)
print(arr[int(input())])