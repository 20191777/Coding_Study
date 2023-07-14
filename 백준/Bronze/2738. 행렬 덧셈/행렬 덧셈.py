n, m = map(int, input().split())

a_l = []

for i in range(n*2):
    a_l.append(list(map(int, input().split())))
# print(a_l)
ans = []
for i in range(n):
    ans.append([x + y for x,y in zip(a_l[i], a_l[i+n])])
    print(' '.join(map(str, ans[i])))