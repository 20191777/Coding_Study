ans = int(input())
c = int(input())

sum = 0
for i in range(c):
    p, cnt = map(int, input().split())
    sum += p*cnt

if(ans == sum):
    print("Yes")
else:
    print("No")