group_num = 0

while True:
    n = int(input())
    if n == 0:
        break
    group_num += 1
    print("Group", group_num)

    names = []
    messages = []
    for _ in range(n):
        data = input().split()
        names.append(data[0])
        messages.append(data[1:])

    nasty = False
    for i in range(n):
        for j in range(n-1):
            if messages[i][j] == 'N':
                nasty = True

                # 자기 위치 (0) - N 인덱스(1) -1 전체인원(5) ) % n 
                a = (i - j - 1 + n) % n
                print(f"{names[a]} was nasty about {names[i]}")

    if not nasty:
        print("Nobody was nasty")

    print("")