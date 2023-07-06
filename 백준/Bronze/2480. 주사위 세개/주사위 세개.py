a, b, c = map(int, input().split())
price = 0
if(a==b==c):
    price = a*1000 + 10000
elif(a==b or a==c or b==c):
    if(a==b or a==c):
        price = a*100 + 1000
    elif (c==b):
        price = c*100 + 1000

else :
    m = max(max(a,b),c)
    price = m*100

print(price)