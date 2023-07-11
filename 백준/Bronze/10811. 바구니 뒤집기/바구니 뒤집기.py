import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

l = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    l_reverse = l[i-1:j]
    l_reverse.reverse()
    l[i - 1:j] = l_reverse

print(' '.join(map(str ,l)))