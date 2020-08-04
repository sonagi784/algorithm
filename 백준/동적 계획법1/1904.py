result = [0, 1, 2]
for i in range(3, 1000001):
    result.append((result[i-1]%15746+result[i-2]%15746)%15746)
print(result[int(input())])