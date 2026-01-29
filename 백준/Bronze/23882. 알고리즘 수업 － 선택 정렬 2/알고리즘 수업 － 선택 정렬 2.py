import sys

n, k = map(int, sys.stdin.readline().split()) # 배열 크기, 교환 횟수
a = list(map(int, sys.stdin.readline().split())) 

cnt = 0

for last in range(n-1, 0, -1):
    # A[1..last]중 가장 큰 수 A[i]를 찾는다
    max_val = max(a[:last + 1])
    max_idx = a.index(max_val)

    # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    if (last != max_idx):
        a[last], a[max_idx] = a[max_idx], a[last]
        cnt += 1

        if cnt == k:
           print(*a)
           break
    
if cnt < k:
    print("-1")