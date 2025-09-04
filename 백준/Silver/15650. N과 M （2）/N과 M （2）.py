
def backtrack():
    # 정답인 경우
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    
    # 아직 정답이 아닌 경우
    for i in range(1, n+1):
        # 안 쓴 숫자고, 마지막에 담은 숫자보다는 큰 숫자
        if (i not in arr) and (len(arr) == 0 or (i > arr[-1])):
            arr.append(i) # 선택
            backtrack() # 백트래킹
            arr.pop() # 돌아가기
        

n, m = map(int, input().split())
arr = []

backtrack()