import sys

input = sys.stdin.readline

t = int(input())
cnt = 0
def recursion(s, l, r, cnt):
    if l>r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        if l != r:
            cnt += 1
        return recursion(s, l+1, r-1, cnt)


def isPalindrome(s):
    cnt = 1
    return recursion(s, 0, len(s)-1, cnt)

for i in range(t):
    s = input().rstrip()
    print(" ".join(map(str, isPalindrome(s))))