ea = 1001
prime_numbers = [True] * ea
for i in range(2, int(ea**0.5)+1):
    if prime_numbers[i] == True:
        for j in range(i*2, ea, i):
            prime_numbers[j] = False
            
prime = []
for i in range(2, int(ea**0.5)+1):
    if prime_numbers[i] == True:
        prime.append(i)
 
composite_numbers = [0] * ea
color = 1
for p in prime:
    for i in range(p*2, ea, p):
        composite_numbers[i] = color
    color += 1
 
import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    res = []
    for i in c:
        res.append(composite_numbers[i])
 
    color = 0
    for r in sorted(list(set(res))):
        color += 1
        for i in range(len(res)):
            if res[i] == r:
                res[i] = color
    print(color)
    print(*res)