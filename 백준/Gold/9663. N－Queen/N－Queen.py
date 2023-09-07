import sys
input = sys.stdin.readline

n = int(input())
row = [0] * n
cnt = 0

def find(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            row[x] = i
            if find(x):
                dfs(x + 1)

dfs(0)
print(cnt)