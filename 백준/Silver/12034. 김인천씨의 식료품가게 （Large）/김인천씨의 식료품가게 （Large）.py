t = int(input())
for i in range(t):
    n = int(input())
    p_list = list(map(int, input().split()))

    result = []
    for p in p_list:
        pi = p*100//75
        if pi in p_list:
            result.append(p)
            p_list.remove(pi)

    print(f"Case #{i+1}: {' '.join(map(str, result))}")