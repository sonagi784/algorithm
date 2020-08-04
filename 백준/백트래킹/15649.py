N, M = map(int, input().split())
check = [False] * N
arr = []

def solve(count):
    if count == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(N):
        if check[i] == False:
            check[i] = True
            arr.append(i+1)
            solve(count+1)
            arr.pop()
            check[i] = False

solve(0)