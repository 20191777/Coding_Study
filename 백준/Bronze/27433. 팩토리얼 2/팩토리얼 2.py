import sys
input = sys.stdin.readline

n = int(input())

ans = 1
i = 0
def factorial(n, ans, i):
    if i == n:
        print(ans)
        return
    ans *= i+1
    i+=1
    factorial(n, ans, i)

factorial(n, ans, i)
# print(result)