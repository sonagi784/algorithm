import sys, collections
input = sys.stdin.readline
 
for _ in range(int(input())):
    s = input().rstrip()
    m = int(input())
    b = list(map(int, input().split()))
    t = [None] * m
    letter = sorted(set(s), reverse=True)
 
    for l in letter:
        zeros = []
        for i in range(len(b)):
            if b[i] == 0:
                zeros.append(i) # index of 0
        if len(zeros) > s.count(l):
            continue
   
        for i in range(len(b)):
            if b[i] != 0:
                b[i] -= sum(map(lambda z:abs(z-i), zeros))
        for zero_idx in zeros:
            b[zero_idx] = -1
            t[zero_idx] = l
 
    print(''.join(t))