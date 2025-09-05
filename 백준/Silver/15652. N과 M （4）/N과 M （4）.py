# 중복조합
# from itertools import combinations_with_replacement

# n, m = map(int, input().split())

# nums = [i for i in range(1, n+1)]

# arr = list(combinations_with_replacement(nums, m))

# for i in arr:
#     print(" ".join(map(str, i)))


# dfs
def dfs():
    if (len(arr) == m):
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        if (len(arr) == 0 or (i >= arr[-1])):
            arr.append(i)
            dfs()
            arr.pop()

n, m = map(int, input().split())
arr = []

dfs()
