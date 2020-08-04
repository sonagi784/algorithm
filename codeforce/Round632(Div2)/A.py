import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    picture = [[None] * m for _ in range(n)]
    if n%2==1 and m%2==1:
        BorW = ['B', 'W']
    elif n%2==0 and m%2==0:
        BorW = ['W', 'B']
    else: #홀짝
        BorW = ['B', 'W']
    
    for i in range(n):
        for j in range(m):
            color = BorW[(i+j)%2]
            picture[i][j] = color
            
    if not (n%2==1 and m%2==1):
        picture[-1][-1] = 'B'
    
    for res in picture:
        print(''.join(res))