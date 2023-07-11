import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    s = sys.stdin.readline().rstrip()
    print(s[0] + s[-1])