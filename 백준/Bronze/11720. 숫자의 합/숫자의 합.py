num = int(input())
digits = int(input())
sum = 0

while(digits>0):
    sum+=digits%10
    digits//=10

print(sum)