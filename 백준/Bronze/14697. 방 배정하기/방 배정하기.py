a, b, c, n = map(int, input().split()) # a, b, c = 방의 정원 / n = 인원수

is_able = False
for i in range(a):
    for j in range(b):
        for k in range(c):
            total = a * i + b * j + c * k

            if total == n:
                is_able = True

if is_able:
    print("1")
else:
    print("0")