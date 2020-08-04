N = int(input())
result = []
stack = []
insert_num = 1
flag = True

for _ in range(N):
    num = int(input())
    while insert_num <= num:
        stack.append(insert_num)
        result.append('+')
        insert_num += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False

print('\n'.join(result) if flag else 'NO')