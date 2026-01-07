n = int(input())
n2 = ~n + 1 # n의 2의 보수

# 32비트로 맞추기
n_32 = n & 0xFFFFFFFF
n2_32 = n2 & 0xFFFFFFFF

# XOR로 서로 다른 비트만 남기고 비트 카운트
print((n_32 ^ n2_32).bit_count())