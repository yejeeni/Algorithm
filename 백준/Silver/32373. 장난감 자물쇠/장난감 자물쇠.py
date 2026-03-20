def solve(): 
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(n):
        # 숫자 i는 무조건 i번에 있어야 함
        # 현재 숫자의 자리 i, 숫자가 위치해야할 자리 nums[i]
        # k칸씩 점프 = 자리를 k로 나눈 나머지가 같은 곳에만 위치 가능
        if i % k != nums[i] % k:
            print("No")
            return
        
    print("Yes")

solve()