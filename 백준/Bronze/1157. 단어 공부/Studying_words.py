s = input().upper()

cnt = {}
l = list(set(s))
for i in range(len(l)):
    cnt[l[i]] = s.count(l[i])

val = list(cnt.values())
m = max(cnt.item(), key= lambda  x:x[1])

g = [k for k, v in cnt.items() if v == m]

if(len(g)>1):
    print("?")
else :
    print(g[0])