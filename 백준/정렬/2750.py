def insertion_sort(num):
    for i in range(1, len(num)):
        j = i - 1
        key = num[i]
        while num[j] > key and j >=0:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = key
    return num
    
def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]  
    return num

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
#print('\n'.join(map(str, bubble_sort(num))))
print('\n'.join(map(str, insertion_sort(num))))