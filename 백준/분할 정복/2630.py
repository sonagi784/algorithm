def check(start_i, start_j, length):
    global zero, one
    color = arr[start_i][start_j]
    flag = True
    for i in range(start_i, start_i+length):
        if not flag:
            break
        for j in range(start_j, start_j+length):
            if color != arr[i][j]:
                flag = False
                check(start_i, start_j, length//2)
                check(start_i+length//2, start_j, length//2)
                check(start_i, start_j+length//2, length//2)
                check(start_i+length//2, start_j+length//2, length//2)
                break

    if flag:
        if color == 0:
            zero += 1
        else:
            one += 1

zero = 0 # white
one = 0 # blue
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
check(0, 0, N)
print(zero, one, sep='\n')