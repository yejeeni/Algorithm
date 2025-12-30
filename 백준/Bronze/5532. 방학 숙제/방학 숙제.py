l = int(input()) # 기간
a = int(input()) # 국어 양
b = int(input()) # 수학 양
c = int(input()) # 국어 가능 최대량
d = int(input()) # 수학 가능 최대량

kor = a // c
math = b // d

if (kor > math):
    if (a % c > 0):
        print(l-kor-1)
    else:
        print(l-kor)
else:
    if (b % d > 0):
        print(l-math-1)
    else:
        print(l-math)