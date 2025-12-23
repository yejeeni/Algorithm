n, m = map(int, input().split())

if m % 2 > 0:
    cut_line = m // 2 + 1
else:
    cut_line = m // 2

result = 0
for _ in range(n):
    m = input()
    cnt = m.count("O")

    if (cnt >= cut_line):
        result += 1
    
print(result)