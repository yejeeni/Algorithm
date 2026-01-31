t = int(input())

for _ in range(t):
    numbers = input()

    result = 0
    count = 1

    for num in numbers[::-1]:
        # 짝수 번째는 2배
        if count % 2 == 0:
            num = int(num) * 2
            
            # 값이 10 이상이면 자릿수합으로 대체
            if num >= 10:
                s = 0
                for n in str(num):
                    s += int(n)
                num = s

        result += int(num)
        count += 1

    if result % 10 == 0:
        print("T")
    else:
        print("F")