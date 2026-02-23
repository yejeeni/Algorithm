n = int(input())
word = input()

result = "NO"

# 문자열 맨앞/끝에서부터 하나씩 늘려가면서 만든 두 부분 문자열은 겹쳐도 무방하며, 부분 문자열의 길이는 1 이상
# 두 부분 문자열은 딱 하나의 문자만 달라야 함

for i in range(n):
    # 맨앞/끝에서 문자열 만들기
    front = word[0:i]
    back = word[n-i:n]

    # 두 문자열의 문자를 차례로 비교
    count = 0
    for j in range(i):
        if front[j] != back[j]:
            count += 1

    # 하나만 다른 경우 YES
    if count == 1:
        result = "YES"
        break

print(result)
