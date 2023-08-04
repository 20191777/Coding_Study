import sys

n = int(sys.stdin.readline().rstrip())
l = []
for _ in range(n):
    l.append(list(reversed(list(map(int, sys.stdin.readline().rstrip().split())))))

l.sort()
for i in range(n):
    print(" ".join(map(str, list(reversed(l[i])))))