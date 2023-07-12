import sys

chess = [1,1,2,2,2,8]

l = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(l)):
    l[i] = chess[i] - l[i]
print(' '.join(map(str ,l)))