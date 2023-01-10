test_case = int(input())

for _ in range(test_case):
    ox = input()
    score = 0
    sum = 0

    for str in ox:
        if(str == 'O'):
            score+=1
            sum+=score
        else:
            score=0
    print(sum)