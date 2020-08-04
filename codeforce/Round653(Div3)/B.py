for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n != 1:
        cnt += 1
        if n >= 6 and n % 6 == 0:
            n = n//6
        elif n >= 3 and n % 3 == 0:
            n = n*2
        else:
            cnt = -1
            break;
    print(cnt)