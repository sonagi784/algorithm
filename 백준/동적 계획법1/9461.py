p = [0, 1, 1, 1, 2 ,2]
for i in range(6, 101):
    p.append(p[i-1] + p[i-5])
for _ in range(int(input())):
    print(p[int(input())])