n, m = map(int, input().split()) # n 수업 수, m 목표 수

students = []
for i in range(n):
    k = int(input()) # 수강생 수
    students += input().split() # 수강생들 학번 모음

# 딕셔너리에 학번 : 수강수 로 정리
dic = {}

for student in students:
    if student in dic:
        dic[student] += 1
    else:
        dic[student] = 1

cnt = 0
for i in dic.values():
    if i >= m:
        cnt += 1

print(cnt) 