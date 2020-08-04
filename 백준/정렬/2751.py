import random

def partition(arr, start, end): # swap(pivot, 큰것들중 가장 작은 상한)
    pivotidx = random.randint(start, end)
    pivotval = arr[pivotidx]
    
    arr[pivotidx], arr[end] = arr[end], arr[pivotidx] # swap(pivotidx, end)
    pivotidx, pivotval = end, arr[end]
    
    storeidx = start #storeidx = 상한값 idx
    for i in range(start, end): #pivot보다 작으면 앞으로, 크면 뒤로
        if arr[i] < pivotval:
            arr[i], arr[storeidx] = arr[storeidx], arr[i]
            storeidx += 1
    arr[storeidx], arr[pivotidx] = arr[pivotidx], arr[storeidx]
    pivotidx = storeidx
    return pivotidx

def quick_sort(arr, start, end):
    if start < end:
        pivotidx = partition(arr, start, end)
        quick_sort(arr, start, pivotidx-1)
        quick_sort(arr, pivotidx+1, end)

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

quick_sort(arr, 0, len(arr)-1)

for i in range(len(arr)):
    print(arr[i])