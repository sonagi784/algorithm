N, M = map(int, input().split())
arr = []

def solve(count):
    if count == M:
        print(' '.join(map(str, arr)))
        return
    
    if count == 0:
        rng = range(N)
    else:
        rng = range(arr[-1]-1, N)
        
    for i in rng:
        arr.append(i+1)
        solve(count+1)
        arr.pop()

solve(0)