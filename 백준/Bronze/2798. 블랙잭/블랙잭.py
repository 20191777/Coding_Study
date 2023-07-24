n, m = map(int, input().split())
nums = list(map(int, input().split()))

ans = []

for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            res = nums[i] + nums[j] + nums[z]
            if res <= m:
                ans.append(res)

print(max(ans))