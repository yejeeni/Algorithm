n = int(input()) # 시간 n
m = int(input()) # 들어있는 차량의 수 m

max_car = m

for i in range(1, n+1):
    # 1분에 입구를 통과한 차의 수와, 출구를 통과한 차의 수
    a, b = map(int, input().split())

    m = m + a - b # 현재 차량 수

    if m < 0:
        max_car = 0
        break
    
    if m > max_car:
        max_car = m
    
print(max_car)