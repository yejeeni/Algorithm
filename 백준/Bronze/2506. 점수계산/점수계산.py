n = int(input())
scores = list(map(int, input().split()))

prev = 0
total = 0
for score in scores:
    if score == 1:
        if prev != 0:
            total += 1 + prev
            prev += 1
        else:
            total += 1
            prev = 1
    else:
        prev = 0

print(total)