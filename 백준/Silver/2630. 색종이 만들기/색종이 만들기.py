"""
규칙: 색이 같으면 1장, 다르면 4등분
나눠진 종이도 같은 규칙이 적용됨 -> 분할(재귀)
조건 만족하면 종료, 아니면 반으로 나눠 같은 문제 반복

분할정복이라 판단한 이유
입력 크기가 2^n이라 정확히 반으로 나눌 수 있음
문제에서 나눈다는 표현이 있기도 하고, 나눈 후에는 똑같은 문제를 반복함
즉, 문제 구조부터 자기 자신을 다시 호출하는 구조


영역을 더 쪼개지 않고 하나의 결과로 확정할 수 있는 조건(반복문을 더 돌리거나 재귀를 더 타지 않고 바로 끝낼 수 있는 종료 조건(base case))이 있는가?
아니면 조건 불만족 시 나누는가?
나눈 후에도 같은 로직을 쓰는가?

YES가 2개 이상 → 분할정복
"""

n = int(input()) # 2, 4, 8, 16, 32, 64, 128 중 1

paper = []
white = 0
blue = 0

for i in range(n):
    paper.append(list(input().split()))
    i+=1

def div(x, y, n): # x좌표, y좌표, 종이 크기
    global white, blue

    color = paper[x][y]

    for j in range(x, n+x): # 종이 크기 꽉 채우려면 n+x까지를 범위로 해야 함
        for k in range(y, n+y):
            if color != paper[j][k]: # 바로 옆 색상과 일치하지 않는 경우
                # 종이를 4개로 분할
                div(x, y, n // 2) # 왼쪽 위
                div(x, y + n // 2, n // 2) # 오른쪽 위
                div(x + n // 2, y, n // 2) # 왼쪽 아래
                div(x + n // 2, y + n // 2, n // 2) # 오른쪽 아래
                return
    
    # 분할이 전부 끝나고 전부 같은 색이 됐을 때
    if color == '1':
        blue += 1
    else:
        white += 1

div(0, 0, n)
print(white)
print(blue)