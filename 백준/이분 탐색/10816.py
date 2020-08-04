def binary_search(arr, value, low, high): #오름차순
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] > value:
        return binary_search(arr, value, low, mid-1)
    elif arr[mid] < value:
        return binary_search(arr, value, mid+1, high)
    else:
        return True

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))
result = []
weight = [0] * (1 + 10000000 + 10000000) # -10000000 ~ 0 ~ 10000000
for idx in cards:
    weight[idx] += 1
for v in nums:
    if binary_search(cards, v, 0, N-1):
        result.append(weight[v])
    else:
        result.append(0)

print(*result)