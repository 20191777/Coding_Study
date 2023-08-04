import sys
input = sys.stdin.readline

N = int(input())
L = []

for i in range(N):
    x, y = map(int, input().split())
    L.append((x, y))

L = sorted(L, key=lambda x: (x[1], x[0]))
for i in range(N):
    print(L[i][0], L[i][1])