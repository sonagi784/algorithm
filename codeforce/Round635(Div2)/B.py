from math import floor
 
for _ in range(int(input())):
    x, n, m = map(int, input().split())
    for _ in range(n):
        if x >= 20:
            x = floor(x/2) + 10
    
    for _ in range(m):
        x = x - 10
    
    print('YES' if x <= 0 else 'NO')