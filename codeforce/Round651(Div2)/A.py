import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    result = (n - n%2) // 2
    print(result)
