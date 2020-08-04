N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
paper = [0, 0, 0]

def cut(starti, startj, length):
    number = arr[starti][startj]
    flag = True

    for i in range(starti, starti+length):
        if flag == False:
            break
        for j in range(startj, startj+length):
            if number != arr[i][j]:
                flag = False
                cut(starti, startj, length//3)
                cut(starti, startj+length//3, length//3)
                cut(starti, startj+(length//3)*2, length//3)
                cut(starti+length//3, startj, length//3)
                cut(starti+length//3, startj+length//3, length//3)
                cut(starti+length//3, startj+(length//3)*2, length//3)
                cut(starti+(length//3)*2, startj, length//3)
                cut(starti+(length//3)*2, startj+length//3, length//3)
                cut(starti+(length//3)*2, startj+(length//3)*2, length//3)
                break;
    if flag:
        paper[number] += 1

cut(0, 0, N)
print(paper[-1], paper[0], paper[1], sep='\n')