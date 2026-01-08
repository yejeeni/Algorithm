nums = []
for _ in range(10):
    nums.append(int(input()))

current_sum = 0
result = 0

for now_num in nums:
    current_sum += now_num

    # current_sum과 이전 합(result) 중 100에 가까운 것 선택
    # 100까지의 거리 계산
    if abs(100 - current_sum) <= abs(100 - result): # 더한값이 100에 더 가까움
        result = current_sum # 더한값으로 result 설정
            
    else:
        break # 이전값으로 result

print(result)