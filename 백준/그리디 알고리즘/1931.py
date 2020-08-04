times = []
for _ in range(int(input())):
    times.append(list(map(int, input().split())))
times.sort(key = lambda e: e[0])
times.sort(key = lambda e: e[1])

now = 0
result = 0
for begin, end in times:
    if now <= begin:
        result += 1
        now = end

print(result)