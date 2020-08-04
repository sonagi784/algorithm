member = []
for _ in range(201):
    member.append([])
    
for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    member[age].append(name)

for i in range(201):
    for name in member[i]:
        print(i, name)