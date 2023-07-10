n, m = map(int, input().split())

bag = [0 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        bag[l] = k

bag = map(str, bag)

print(' '.join(bag))