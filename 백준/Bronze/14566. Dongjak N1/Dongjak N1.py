n = int(input()) # 정차 횟수
a = list(map(int, input().split())) # 정류장 좌표

a.sort()

min = 40000000
count = 0

for i in range(n-1):
    diff = a[i+1] - a[i]

    if diff < min:
        min = diff
        count = 1
        
    elif diff == min:
        count += 1

print(min, count)