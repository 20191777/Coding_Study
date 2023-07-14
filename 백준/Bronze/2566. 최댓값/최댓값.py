l = []
for i in range(9):
    l.append(list(map(int, input().split())))

m = []
for i in range(9):
    m.append(max(l[i]))
ans = max(m)
print(ans)
ans_a = m.index(ans)
print(ans_a+1, end=" ")
print(l[ans_a].index(ans)+1)