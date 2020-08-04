import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split()))) #O(NlogN)
    CHECK = False
    save_sum = sum(a) #O(N)
    for i in range(n): #O(N)
        if save_sum / (n-i) >= x:
            CHECK = True
            break
        else:
            save_sum -= a[i]
    print(n-i if CHECK else 0)