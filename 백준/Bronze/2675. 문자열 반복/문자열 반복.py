test_case = int(input())

for t in range(test_case):
    repeat, str = input().split() 

    for i in range(len(str)):
        # print() 줄바꿈 제거
        print(str[i]*int(repeat), end="")
    print()