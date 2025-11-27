"""
N개의 자연수 중에서 M개를 고른 수열 (1 ≤ M ≤ N ≤ 8)


첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어진다. 
입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.
수열은 오름차순으로 출력

N M
3 1
3개의 자연수에서 길이가 1인 수열을 구할 것
4 5 2

2
4
5
"""

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = []

def backtracking():
    # 종료 조건
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    # n개의 자연수만큼 반복
    for i in range(n):
        if nums[i] in arr: # 이미 들어있는 숫자인 경우 패스
            continue

        # 없는 숫자일 경우
        arr.append(nums[i]) # 해당 숫자 추가
        backtracking()
        arr.pop()

backtracking()