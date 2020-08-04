import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            even.append((a[i], i+1))
        else:
            odd.append((a[i], i+1))
 
    if (len(even) * len(odd)) % 2 == 1:
        even.pop()
        odd.pop()
    else:
        if len(even) > len(odd):
            even.pop()
            even.pop()
        else:
            odd.pop()
            odd.pop()
    
    for i in range(0, len(even), 2):
        print(even[i][1], even[i+1][1])
    for i in range(0, len(odd), 2):
        print(odd[i][1], odd[i+1][1])