n = int(input())
cnt = 4
for i in range(n):
    cnt = (cnt-2**(2*i))**2

print(cnt)