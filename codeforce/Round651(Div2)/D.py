def check(x, p):
    ans = 0
    for i in range(n):
        if a[i] <= x or ans % 2 == p:
            ans += 1
        
        if ans >= k:
            return True
    return False
 
n, k = map(int, input().split())
a = list(map(int, input().split()))
lo, hi = min(a), max(a)
while lo < hi:
    x = (lo+hi) // 2
    if check(x, 0) or check(x, 1):
        hi = x
    else:
        lo = x+1
print(lo)