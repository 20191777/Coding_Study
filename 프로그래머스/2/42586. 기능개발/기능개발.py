import math

def solution(progresses, speeds):
    dates = []
    for i in range(len(progresses)):
        dates.append(math.ceil((100 - progresses[i]) / speeds[i]))
    answer = []
    cnt = 1
    i = 0
    # for i in range(len(dates) - 1):

    while i < len(dates) - 1:
        k = i
        for j in range(i + 1, len(dates)):
            #print(dates[i], dates[j])
            #print("i = ", i)

            if dates[k] < dates[j] and sum(answer) < len(dates):
                #print(1)
                answer.append(cnt)
                cnt = 1
                if j == len(dates) - 1:
                    answer.append(cnt)
                i += 1
                break
            elif dates[k] >= dates[j]:
                #print(2)
                cnt += 1
                i += 1
            if dates[k] >= dates[j] and j == len(dates) - 1 and sum(answer) < len(dates):
                #print(3)
                answer.append(cnt)

    #print(answer)

    return answer