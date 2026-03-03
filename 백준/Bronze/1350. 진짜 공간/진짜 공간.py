import math

n = int(input())
sizes = list(map(int, input().split()))
cluster = int(input())

result = 0
for size in sizes:
    count = math.ceil(size / cluster) 
    result += count * cluster

print(result)