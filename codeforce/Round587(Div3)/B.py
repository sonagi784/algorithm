n = int(input())
temp = list(map(int, input().split()))
a = []
for i in range(len(temp)):
    a.append((temp[i], i+1))
a.sort(key=lambda s:s[0], reverse=True)
 
result = 0
order = []
for i in range(len(a)):
    result += a[i][0] * i + 1
    order.append(a[i][1])
print(result)
print(*order)