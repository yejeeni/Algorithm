a, b = map(int, input().split())

# 4각형부터만 가능
if a < 4:
    a = 4

# a, b를 범위 내 짝수로 맞춰주기
if a % 2 != 0:
    a += 1

if b % 2 != 0:
    b -= 1

if a > b:
    print(0)
else:
    #개수(첫항+끝항)/2
    print(((b-a)//2+1)*(a+b)//2)