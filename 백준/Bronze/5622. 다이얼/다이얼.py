import sys

s = sys.stdin.readline().rstrip()

ans = 0

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in range(len(s)):
    for d in dial:
        if(d.count(s[i]) >= 1):
            ans += (dial.index(d) + 3)

print(ans)