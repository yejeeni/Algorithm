array = [[0 for _ in range(100)] for _ in range(100)]

for i in range(4):
    # 왼쪽 아래 꼭짓점, 오른쪽 위 꼭짓점
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            array[x][y] = 1

result = 0
for row in array:
    result += sum(row)
print(result)