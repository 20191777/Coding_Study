import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(" "*(n-i-1), end='')
    print((i*2+1)*"*")

for i in range(n-2, -1, -1):
    print(' ' * (n-2-i), end=' ')
    print('*' * (2*i+1))