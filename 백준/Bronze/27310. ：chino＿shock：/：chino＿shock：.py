# 전체 길이 + 콜론 개수 + 언더바 개수 * 5

name = input()

print(len(name) + name.count(":") + name.count("_") * 5)