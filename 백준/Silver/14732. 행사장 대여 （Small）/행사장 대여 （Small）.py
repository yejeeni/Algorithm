n = int(input())

area = [[0] * 501 for _  in range(501)] # 500*500 사이즈

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    # 영역 체크
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = 1

result = 0
for arr in area:
    result += sum(arr) # 한줄에 색칠돼있는 칸 더하기

print(result)