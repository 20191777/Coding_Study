n = int(input())

for i in range(1, n+1):
    sum = 0
    sum += i
    s = str(i)

    for j in range(len(s)):
        sum += int(s[j])
            # print(s[j])
    # print("i :",i)
    # print("sum :", sum)
    if sum == n:
        print(i)
        break
    elif sum != n and i == n:
        print(0)
        break