def getcnt(LAN, mid):
    result = 0
    for lan in LAN:
        result += (lan // mid)
    return result

def parametic_search(LAN, N, left, right):
    while(left <= right):
        mid = (left + right) // 2
        cnt = getcnt(LAN, mid)
        if cnt >= N:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return result

K, N = map(int, input().split())
LAN = []
for k in range(K):
    LAN.append(int(input()))
LAN.sort()
left = 1
right = max(LAN) # <--  min(LAN)은 왜 안되나요
print(parametic_search(LAN, N, left, right))