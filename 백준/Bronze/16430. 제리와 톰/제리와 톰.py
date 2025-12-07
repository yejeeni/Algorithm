import math

a,b = map(int, input().split()) # 1kg 의 a/b 만큼 훔쳐감
# print(b-a, b)

p = b - a
q = b
g = math.gcd(p, q) # p와 q의 최대공약수 구하기

print(p//g, q//g)
