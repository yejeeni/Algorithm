a, b, c, n = map(int, input().split()) # a, b, c = 방의 정원 / n = 인원수

is_able = False
for i in range(n // a + 1): # 각 방의 개수는 최대 n // 정원 까지
    for j in range(n // b + 1):
        for k in range(n // c + 1):
            total = a * i + b * j + c * k

            if total == n:
                is_able = True

if is_able:
    print("1")
else:
    print("0")
