def binary_search(arr, value, low, high): #오름차순
    if low > high:
        print('0')
        return;
    mid = (low + high) // 2
    if arr[mid] > value:
        binary_search(arr, value, low, mid-1)
    elif arr[mid] < value:
        binary_search(arr, value, mid+1, high)
    else:
        print('1')

N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
A.sort()
for i in range(M):
    binary_search(A, nums[i], 0, N-1)