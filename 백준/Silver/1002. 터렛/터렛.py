"""
중심이 (a, b)인 원의 방정식: (x-a)^2 + (y-b)^2 = r^2
두 점의 거리: d = ( (x1-x2)^2 + (y1-y2)^2 )^(1/2)

1) 겹치는 게 없는 경우
    1. 떨어져있음: d > r + r'
    2. 한 원이 다른 원의 내부에 있음: d < r - r'
    3. 2에 두 원이 중심이 같음: d=0 추가 ###

2) 겹치는 게 하나
    1. 외접: d = r + r' 
    2. 내접: d = r - r' 

3) 겹치는 게 두 개
    r - r' < d < r + r' ###

4) 겹치는 게 무한
    d = 0이고 r = r' ###
"""

import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x1-x2)**2 + (y2-y1)**2)
      
    if (d==0): # 중심이 같을 때
        if (r1 == r2): # 두 원이 겹치는 경우
            print(-1)
        else: # 두 원이 중심만 같은 경우
            print(0)
    elif (abs(r1 - r2) < d < r1 + r2): # 두 지점에서 만나는 경우
        print(2)
    elif (d > r1 + r2 or d < abs(r1 - r2)): # 두 원이 떨어져있거나, 한 원이 다른 원의 내부에 있는 경우
        print(0)
    else: # 외접하거나 내접
        print(1)