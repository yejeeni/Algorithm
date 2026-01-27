"""
한 단어를 재배열해 다른 단어를 만들 수 있어야 한다. ->  아나그램 판별이므로 sorted로 비교
두 단어의 첫 글자와 마지막 글자는 서로 동일해야 한다.
각 단어에서 모음(a, e, i, o, u)을 제거한 문자열은 동일해야 한다.

시간이나 비용을 고려해서 순서를 바꾸는거도...
"""

n = int(input())

str1 = input()
str2 = input()

is_duramuri = True

# 구성 요소가 같은지 점검
if sorted(str1) != sorted(str2):
    is_duramuri = False

# 첫 글자와 마지막 글자가 동일한지 점검
if str1[0] != str2[0] or str1[-1] != str2[-1]:
    is_duramuri = False

# 모음 제거 문자열이 동일한지 점검
result1 = [char for char in str1 if char not in "aeiou"]
result2 = [char for char in str2 if char not in "aeiou"]

if result1 != result2:
    is_duramuri = False

if is_duramuri:
    print("YES")
else:
    print("NO")