import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    stk = []
    s = input().rstrip()
    isVPS = True

    for i in s:
        if i == '(':
            stk.append('(')
        if i == ')':
            if stk:
                stk.pop()
            elif not stk:
                isVPS = False
                break
                
    if not stk and isVPS:
        print('YES')
    elif stk or not isVPS:
        print('NO')