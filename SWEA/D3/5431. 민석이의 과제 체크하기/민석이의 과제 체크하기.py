t = int(input())

for i in range(t):
    print("#" + str(i+1), end = " ")
    cnt, submit_cnt = map(int, input().split())
    submitted = list(map(int, input().split()))

    ans = []
    for i in range(1, cnt+1):
        if submitted.count(i) == 0:
           ans.append(i)

    print(" ".join(map(str, ans)))
