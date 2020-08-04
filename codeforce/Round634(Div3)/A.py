import sys
input = sys.stdin.buffer.readline
for _ in range(int(input())):
    n = int(input())
    print(n//2 - 1 + n%2)