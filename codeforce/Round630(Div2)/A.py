for _ in range(int(input())):
    a, b, c, d = map(int, input().split()) # left right down up
    x, y, x1, y1, x2, y2 = map(int, input().split()) # x1 < x < x2  and  y1 < y < y2
    left, right, down, up = a-b, b-a, c-d, d-c
    leftbound, rightbound, downbound, upbound = x-x1, x2-x, y-y1, y2-y
 
    if leftbound == rightbound == 0 and (a != 0 or b != 0):
        print('No')
        continue
    if downbound == upbound == 0 and (c != 0 or d != 0):
        print('No')
        continue 
 
    if left<=leftbound and right<=rightbound and down<=downbound and up<=upbound:
        print('Yes')
    else:
        print('No')