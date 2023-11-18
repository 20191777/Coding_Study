t = int(input())

for i in range(t):
    print("#" + str(i+1), end = " ")
    a,b = map(int,input().split())
    print(a+b)