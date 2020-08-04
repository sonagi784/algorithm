import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    s = input().rstrip()
    result = s[0]
    for i in range(1, len(s)-1, 2):
        result += s[i]
    result += s[-1]
    print(result)