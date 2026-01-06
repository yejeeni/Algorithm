n, k, p = map(int, input().split())
# n*k개 빵. k개씩 묶어서 판매. k개 중 불량은 p 미만이어야 함

bread = list(map(int, input().split()))

cnt = 0

for i in range(0, n*k, k):
    # 묶음으로 인덱스 슬라이싱 
    b_n = bread[i:i+k]
    
    if (b_n.count(0) < p):
        cnt += 1
    
print(cnt)