l = {i:0 for i in range(1, 31)}

a = []
for _ in range(28):
    k = int(input())
    l[k] = k

for i in range(1, 31):
    if(l[i]==0):
        print(i)
