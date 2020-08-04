def sol(p):
    arr = sorted(p)
    for i in range(len(arr)):
        if arr[i] != (i+1):
            return False
    return True
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a) 
    res = []
    # l1, l2 = mx, n-mx or n-mx, mx
    # p1, p2 = a[0:n-mx], a[n-mx:n] or a[0:mx], a[mx:n]
    p1, p2 = a[0:n-mx], a[n-mx:n]
    if sol(p1) and sol(p2):
        res.append(n-mx)
 
    p1, p2 = a[0:mx], a[mx:n]
    if sol(p1) and sol(p2):
        res.append(mx)
 
    res = set(res)
    
    print(len(res))
    for a in res:
        print(a, n-a)