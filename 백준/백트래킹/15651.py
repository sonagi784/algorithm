N, M = map(int, input().split())
arr = []

def solve(count):
    if count == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(N):
        arr.append(i+1)
        solve(count+1)
        arr.pop()

solve(0)