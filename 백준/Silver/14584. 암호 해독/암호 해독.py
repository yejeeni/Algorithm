message = input()
n = int(input())

words = []
for _ in range(n):
    words.append(input()) # 이중 하나의 단어가 들어있음


# 몇 칸 뒤 알파벳으로 바꾸는지를 모름
for i in range(26): # 알파벳 26자. 최대 26칸 뒤 알파벳으로 변경 가능
    # 암호문 복호화
    result = ""

    for char in message:
        # a를 0으로 두기 위해 ord(char) - ord('a') 후, i만큼 이동
        # % 26으로 26자 안으로 넣기
        # ord('a') 더해서 아스키코드 a 위치로 보정
        key = (ord(char) - ord('a') + i) % 26 + ord('a')
        result += chr(key)

    for word in words:
        if word in result:
            print(result)
            break
