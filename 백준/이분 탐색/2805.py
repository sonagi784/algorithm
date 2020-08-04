# tree : 집에 가져가는 나무의 길이 (M 이상 가져가야함)
# H: 절단기에 설정한 높이
# heights : 각 나무의 높이
def gettree(heights, H):
    tree = 0
    for height in heights:
        if height > H:
            tree += (height - H)
    return tree

# mid : 자르기로 설정한 높이
# M : 가져가야할 나무의 최소길이
def parametic_search(heights, M, left, right):
    while(left <= right):
        mid = (left + right) // 2
        tree = gettree(heights, mid)
        if tree >= M: # 너무 많이 잘랐다, 설정높이가 너무 낮다 == 좀 덜 자르자, 설정높이를 올리자
            H = mid
            left = mid + 1
        else: # 너무 적게 잘랐다, 설정높이가 너무 높다 == 좀 많이 자르자, 설정높이를 낮추자
            right = mid - 1
            
    return H

N, M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
left = 0
right = max(heights)
print(parametic_search(heights, M, left, right))