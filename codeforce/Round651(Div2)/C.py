import sys
input = sys.stdin.readline
#Ashishgup moves first
 
def win():
    print('Ashishgup')
def lose():
    print('FastestFinger')
 
def isprime(n):
    for i in range(2, min(50000, n)):
        if n % i == 0:
            return False
    return True
 
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        lose()
    elif n == 2:
        win()
    elif n % 2 != 0: # odd
        win()
    else: # even
        #n % 2 == 0:            
        #2^n(lose) 
        #2*p(lose - p is prime), 2*p'*odd(win - p not prime)   
        #4*odd(win)
        n = n//2
        if n%2 != 0: # 2*p(lose) / 2*p'*odd(win)
            if isprime(n):
                lose()
            else:
                win()
        else: # 2^n / 4*odd
            while n%2 == 0: n = n//2
            if n == 1: lose()
            else: win()