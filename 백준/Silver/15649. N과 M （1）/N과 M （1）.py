"""
순열?
"""

from itertools import permutations

n, m = map(int, input().split()) # 1부터 n까지 자연수 중에, 중복 없이 m개를 고른 수열
nums = [i for i in range(1, n+1)]

p = list(permutations(nums, m))

for i in p:
    print(' '.join(map(str, i)))