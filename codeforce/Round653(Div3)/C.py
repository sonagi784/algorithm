for _ in range(int(input())):
    n = int(input())
    s = list(input())
 
    cnt = 0
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                cnt = 0
                result += 1
    print(result)