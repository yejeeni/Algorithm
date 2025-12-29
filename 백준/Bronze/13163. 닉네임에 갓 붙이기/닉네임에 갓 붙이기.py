n = int(input())

for _ in range(n):
    nickname = list(input().split())
    nickname[0] = "god"

    for i in nickname:
        print(i, end="")
    print()