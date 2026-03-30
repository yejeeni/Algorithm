import sys

def heap_sort(a): # a[1..n]을 정렬한다.
    build_min_heap(a, n)
    global count
    for i in range(n, 1, -1):
        a[i], a[1] = a[1], a[i]  # 원소 교환
        count += 1
        if count == target:
            print(min(a[1], a[i]), max(a[1], a[i]))
            sys.exit(0)
        heapify(a, 1, i-1)


def build_min_heap(a, n):
    for i in range(n//2, 0, -1):
        heapify(a, i, n)


# A[k]를 루트로 하는 트리를 최소 힙 성질을 만족하도록 수정한다.
# A[k]의 두 자식을 루트로 하는 서브 트리는 최소 힙 성질을 만족하고 있다.
# n은 배열 A의 전체 크기이며 최대 인덱스를 나타낸다.
def heapify(a, k, n):
    left = 2*k
    right = 2*k + 1

    if (right <= n):
        if (a[left] < a[right]):
            smaller = left
        else:
            smaller = right

    elif (left <= n):
        smaller = left

    else: 
        return

    # 최소 힙 성질을 만족하지 못하는 경우 재귀적으로 수정한다.
    if (a[smaller] < a[k]):
        a[k], a[smaller] = a[smaller], a[k]
        global count 
        count += 1
        if count == target:
            print(min(a[smaller], a[k]), max(a[smaller], a[k]))
            sys.exit(0)
        
        heapify(a, smaller, n)
    
n, target = map(int, input().split())
a = [0] + list(map(int, input().split())) # 수도코드가 인덱스 1부터 시작하므로 맞춰줌
count = 0

heap_sort(a)

print(-1)