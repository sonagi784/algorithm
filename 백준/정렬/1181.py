N = int(input()) 
arr = []

for _ in range(51): 
    arr.append(set()) 
    
for _ in range(N): 
    string = input() 
    arr[len(string)].add(string) 
    
for i in range(51): 
    arr[i] = sorted(list(arr[i]))
    
for i in range(51):
    for output in arr[i]: 
        print(output)