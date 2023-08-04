n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

l.sort()
for i in range(n):
    print(" ".join(map(str, (l[i]))))