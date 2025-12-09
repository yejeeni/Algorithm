str, dex, int, luk, n = map(int, input().split())

total = str + dex + int + luk

if total >= n*4:
    print(0)
else:
    print(n*4 - (str + dex + int + luk))