while(True):
    m, a, b = map(int, input().split())
    if m == a == b == 0:
        break

    diff = round((m*(b-a)) / (a*b)*3600)

    hour = diff // 3600 
    minute = (diff % 3600) // 60
    sec = diff % 60
    print(f"{hour}:{minute:02d}:{sec:02d}")