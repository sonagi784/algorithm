import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even_wrong = 0
    odd_wrong = 0
 
    for i in range(0, n, 2): # even
        if a[i]%2 == 1:
            even_wrong += 1
    for i in range(1, n, 2): # odd
        if a[i]%2 == 0:
            odd_wrong += 1
    
    print(even_wrong if even_wrong == odd_wrong else -1)