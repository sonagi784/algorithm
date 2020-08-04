from math import gcd
 
n = int(input())
a = list(map(int, input().split()))
maxval = max(a)
 
# get z
theft = [maxval - v for v in a]
z = 0
for v in theft:
    z = gcd(z, v)
 
# get y
a = [tmp//z for tmp in a]
maxval = max(a)
a = [tmp - maxval for tmp in a]
y = -1 * sum(a)
print(y, z)