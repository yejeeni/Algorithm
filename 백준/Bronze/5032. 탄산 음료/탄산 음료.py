e, f, c = map(int, input().split())

t = e + f
result = 0

while(t >= c):
    result += t // c
    t = t // c + t % c # 새로 교환해서 마시고 나온 빈 병 + 교환 못하고 남은 빈 병

print(result)