import sys

n = int(input())
medicines = dict()
for _ in range(n):
    effect, name = map(int, input().split())
    medicines[effect] = name # 효과: 이름

r = int(input())
for _ in range(r):
    is_broken = False
    
    ls = list(map(int, input().split())) # 개수, 증상1, 증상2, ...
    s_list = ls[1:] # 증상 리스트

    result = []
    for s in s_list:
        if s in medicines:
            result.append(medicines[s])
        else:
            print("YOU DIED")
            is_broken = True
            break
    
    if not is_broken:
        print(*result)