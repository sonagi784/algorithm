def pow(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        temp = pow(a, b//2, c)
        return (temp * temp) % c
    else:
        temp = pow(a, b//2, c)
        return (a * temp * temp) % c

a, b, c = map(int, input().split())
print(pow(a, b, c))
