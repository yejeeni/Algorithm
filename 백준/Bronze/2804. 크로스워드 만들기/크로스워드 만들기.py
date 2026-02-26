a, b = map(str, input().split())

for i in range(len(a)):
    if a[i] in b:
        a_idx = b.index(a[i]) # 세로 단어 b에서 교차하는 위치 (가로 단어 a가 들어갈 행)
        b_idx = i # 가로 단어 a에서 교차하는 위치 (세로 단어 b가 들어갈 열)
        break

for i in range(len(b)):
    if i == a_idx:
        print(a)
        
    else:
        for j in range(len(a)):
            if j == b_idx:
                print(b[i], end='')
            else:
                print('.', end='')
        print('')