for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    check = [False] * (n + 105)
    for idx in range(n):
        check[a[idx]] = True
    idx = 1
    while x>=0:
        if check[idx] == False:
            x -= 1
        idx += 1
    print(idx-2)