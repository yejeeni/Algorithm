n, t = map(int, input().split()) # t 도착시간
result = []

for _ in range(n):
    s, i, c = map(int, input().split()) # 시작시각, 간격, 대수
    buses = [s + (i * c) for c in range(c)] # 모든 배차시간
    if buses[-1] < t:
        continue

    for bus in buses:
        if bus >= t:
            result.append(bus)
            break

if len(result) > 0:
    print(min(result)-t)
else:
    print(-1)
