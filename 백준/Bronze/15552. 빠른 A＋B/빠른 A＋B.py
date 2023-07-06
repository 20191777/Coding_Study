import sys

t = int(sys.stdin.readline().rstrip('\n'))

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)