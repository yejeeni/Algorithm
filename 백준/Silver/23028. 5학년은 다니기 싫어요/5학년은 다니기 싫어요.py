# 21년 2학기까지 n학기동안 전공 a, 전체 b 이수
# 한 학기당 최대 6과목, 과목당 3학점
# 8학기 안에 전공 66 포함 총 130을 해야 함

n, a, b = map(int, input().split()) # 마친 학기 n, 이수 전공 학점 a, 전체 이수 학점 b

s = [list(map(int, input().split())) for _ in range(10)] # 전공, 비전공

if a >= 66 and b >= 130:
    print("Nice")
else:
    for i in range(8-n):
        # 전공
        a += s[i][0] * 3
        b += s[i][0] * 3

        # 교양
        if s[i][0] < 6:
            b += (min(6-s[i][0], s[i][1])) * 3

    if a >= 66 and b >= 130:
        print("Nice")
    else:
        print("Nae ga wae")