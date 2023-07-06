import sys
n = int(sys.stdin.readline().rstrip('/n'))
l = list(map(int, sys.stdin.readline().split()))
ans = int(sys.stdin.readline().rstrip('/n'))

print(l.count(ans))