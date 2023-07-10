import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

bag = {i:i for i in range(1, n+1)}
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    a = bag[i]
    bag[i] = bag[j]
    bag[j] = a

print(' '.join(map(str, bag.values())))