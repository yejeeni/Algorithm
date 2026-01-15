n = int(input())

now_num = n
cnt = 0

while True:

    ten = now_num // 10
    one = now_num % 10
    total_sum = ten + one

    # 새로운 수
    now_num = one * 10 + total_sum % 10

    cnt += 1
    if now_num == n:
        break

print(cnt)