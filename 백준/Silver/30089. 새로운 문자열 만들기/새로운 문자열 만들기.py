t = int(input())

for i in range(t):
    s = input()
    
    for j in range(len(s)):
        # 앞에서부터의 문자
        word= s[:j]

        x = s + word[::-1]

        if x == x[::-1]:
            break

    print(x)