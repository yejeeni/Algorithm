import re

n = input()
s = list(map(int, re.split(r'[.|:#]', input())))

print(sum(s))