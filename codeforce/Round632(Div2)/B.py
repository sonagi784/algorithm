
import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    check = [False, False, False] # [0, 1, -1]
    result = 'YES'
    
    if a[0] != b[0]:
        print('NO')
        continue
 
    if a[0] == 0 or a[0] == 1 or a[0] == -1:
        check[a[0]] = True
    for i in range(1, n):
        if b[i] > a[i] and check[1] == True:
            None
        elif b[i] == a[i]:
            None
        elif b[i] < a[i] and check[-1] == True:
            None
        else:
            result = 'NO'
            break;
        
        if a[i] == 0 or a[i] == 1 or a[i] == -1:
            check[a[i]] = True
        
    print(result)