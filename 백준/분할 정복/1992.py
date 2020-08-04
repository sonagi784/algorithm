N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))

def quad(starti, startj, length):
    BW = arr[starti][startj]
    flag = True
    for i in range(starti, starti+length):
        if flag == False:
            break
        for j in range(startj, startj+length):
            if BW != arr[i][j]:
                flag = False
                print('(', end='')
                quad(starti, startj, length//2)
                quad(starti, startj+length//2, length//2)
                quad(starti+length//2, startj, length//2)
                quad(starti+length//2, startj+length//2, length//2)
                print(')', end='')
                break
    if flag:
        print(BW, end='')

quad(0, 0, N)