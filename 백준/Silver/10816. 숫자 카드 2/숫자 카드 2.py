import sys
input = sys.stdin.readline

N = int(input())
card = [*map(int, input().split())]
M = int(input())
t = [*map(int, input().split())]

cnt = {}
for c in card:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

for i in t:
    result = cnt.get(i)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")