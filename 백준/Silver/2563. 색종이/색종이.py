arr = [[0 for _ in range(101)]for _ in range(101)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    for r in range(x, x+10):
        for c in range(y, y+10):
            arr[r][c] = 1

    ans = 0
    for i in arr:
        ans += i.count(1)
print(ans)