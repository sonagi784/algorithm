swap = dict()
swap['a'] = 'b'
swap['b'] = 'a'
 
n = int(input())
s = list(input())
cnt = 0
for i in range(0, n, 2):
    if s[i] == s[i+1]:
        cnt += 1
        s[i] = swap[s[i]]
    
print(cnt)
print(''.join(s))
