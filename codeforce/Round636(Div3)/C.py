import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    case1 = []
    case2 = []
    check = False
    for i in range(n):
        if a[i] > 0:
            start = i
            now = a[i]
            check = True
            break
    if check:
        for i in range(start+1, n):
            if a[i]*now >= 0: # + +, - -
                now = max(now, a[i])
            else: # + -, - +
                case1.append(now)
                now = a[i]
        if len(case1) == 0 or now != case1[-1]:
            case1.append(now)
    
    check = False
    for i in range(n):
        if a[i] < 0:
            start = i
            now = a[i]
            check = True
            break
    if check:
        for i in range(start+1, n):
            if a[i]*now >= 0:
                now = max(now, a[i])
            else:
                case2.append(now)
                now = a[i]
        if len(case2) == 0 or now != case2[-1]:
            case2.append(now)
    
    if len(case1) > len(case2):
        result = case1
    elif len(case1) < len(case2):
        result = case2
    else:
        result = case1 if sum(case1)>sum(case2) else case2
    print(sum(result))