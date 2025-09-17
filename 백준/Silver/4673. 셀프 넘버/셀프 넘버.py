nums = list(range(1, 10000)) # 전체 숫자
non_self_nums = [] # 셀프 넘버가 아닌 숫자

for num in nums: # 전체 수 반복
    sum = num
    for n in str(num): # 숫자의 자리수만큼 반복
        sum += int(n)
    # d(n) 계산 끝

    non_self_nums.append(sum) # 결과는 셀프넘버가 아니므로 추가

for i in range(1, 10000):
    if i not in non_self_nums:
        print(i)