while(True):
    n = int(input())
    if n == 0:
        break

    arr = []
    for i in range(n):
        arr.append(input())

    # 각 단어를 소문자로 변환한 값을 기준으로 정렬
    arr.sort(key=str.lower)

    # 길이를 기준으로 하고 싶다면 key=len
    # 익명함수 lamda도 활용 가능 (예: 마지막 글자 기준 정렬 시 key=lambda x: x[-1])
    # 여러 조건으로 정렬도 가능. 예: 길이 순 정렬하는데, 길이가 같으면 사전 순 정렬 arr.sort(key=lambda x: (len(x), x.lower()))
    print(arr[0])
