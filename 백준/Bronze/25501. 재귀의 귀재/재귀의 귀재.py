def recursion(s, l, r, count):
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s, count):
    return recursion(s, 0, len(s)-1, count)

t = int(input())
for i in range(t):
    count = 1
    print(*isPalindrome(input(), count))