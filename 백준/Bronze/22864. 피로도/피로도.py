# 하루 한 시간 단위로 일을 하거나 쉼
# 일하면 피로도 +A. 업무처리량 B
# 쉬면 피로도 -C
# 피로도 한도 m

a, b, c, m = map(int, input().split())
x = 0 # 현재 피로도
t = 0 # 처리한 총 업무량

for i in range(24):
    if x > m:
        break

    # 일하기
    else:
        # 일할 수 있음
        if x + a <= m:
            t += b # 업무처리
            x += a # 피로도 증가
        # 할 수 없음 -> 쉬어야 함
        else: 
            x -= c
            # 피로도가 음수가 되면 0으로 보정
            if x < 0:
                x = 0


print(t)