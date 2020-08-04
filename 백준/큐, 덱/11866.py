def nextidx(idx):
    if idx >= len(human) - 1:
        return 0
    return idx + 1

N, K = map(int, input().split()) # 0~ N-1  /  K-1회 nextidx
idx = 0
human = []
order = []

for i in range(1, N+1):
    human.append(i)
    
for i in range(N):
    for _ in range(K-1):
        idx = nextidx(idx)
    order.append(human[idx])
    del human[idx]
    if idx == len(human):
        idx = 0

result = '<'
for i in range(len(order)-1):
    result += str(order[i]) + ', '
result += str(order[-1])
result += '>'
print(result)