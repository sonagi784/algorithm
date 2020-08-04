for T in range(int(input())):
    p = 0
    string = list(input())
    for i in range(len(string)):
        if string[i] == '(':
            p += 1
        elif p == 0:
            p = 1 #print('NO')
            break;
        else:
            p -= 1
    
    if p == 0:
        print('YES')
    else:
        print('NO')
