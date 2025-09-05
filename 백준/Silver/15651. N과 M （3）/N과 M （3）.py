# 중복순열 라이브러리 이용
# from itertools import product

# n, m = map(int, input().split())

# nums = [i for i in range(1, n+1)] # 1부터 n까지 숫자들

# arr = list(product(nums, nums))

# for i in arr:
#     print(" ".join(map(str, i)))


# DFS
def dfs():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        arr.append(i)
        dfs()
        arr.pop()

n, m = map(int, input().split())
arr = []

dfs()