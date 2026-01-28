s_y, s_m, s_d = map(int, input().split()) # 입사일
e_y, e_m, e_d = map(int, input().split()) # 미래의 특정 날짜

# 얻을 수 있는 연차/월차 개수, 근무기간

# 근무기간 계산
days = (e_y - s_y) * 360 + (e_m - s_m) * 30 + (e_d - s_d)

# 월차 계산
result_m = days // 30
if result_m > 36:
    result_m = 36

# 연차 계산
# A 계산
# 1: 0년차에 
# 2: 2n+1 = 2+1 = 3년차에
# 3: 2*2+1 = 4+1 = 5년차에... 0 3 5 7 ... (n-1)/2
result_y = 0
for n in range(1, days // 360 + 1):
    A = (n-1) // 2
    result_y += A + 15

print(result_y, result_m)
print(f"{days}days")