exp = input().split('-')
newexp = []
for e in exp:
    num = e.split('+')
    newnum = []
    for n in num:
        n = n.lstrip('0')
        newnum.append(n)
    newexp.append(sum(map(int, newnum)))
    newexp.append('-')

del newexp[-1]
print(eval(''.join(map(str, newexp))))