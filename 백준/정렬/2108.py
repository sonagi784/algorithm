N = int(input()) # N은 홀수
arr = []
for i in range(N):
    arr.append(int(input()))

print(round(sum(arr)/N)) # 산술평균 O(N)

arr.sort()
print(arr[N//2]) # 중앙값 O(NlogN)

count = [0] * 8001
for i in range(N):
    count[arr[i]] += 1 # O(N)
maxfreq = max(count)
maxarr = []
for i in range(-4000, 4001): # -4000 ~ 4000 , k = 8001, O(k)
    if maxfreq == count[i]:
        maxarr.append(i)
print(maxarr[0] if len(maxarr) == 1 else maxarr[1]) #최빈값 O(N+k)

print(arr[-1] - arr[0]) # 범위 O(N)

#O(N + NlogN + k)