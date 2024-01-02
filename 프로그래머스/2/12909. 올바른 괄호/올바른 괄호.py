def solution(s):
    answer = True
    cnt = 0
    for i in range(len(s)):
        if s[0] != "(" or s[-1] != ")" or len(s) % 2 != 0:
            #print("x")
            answer = False
            break
        elif s[i] == "(":
            cnt += 1
        elif s[i] == ")" and cnt > 0:
            cnt -= 1

    if cnt != 0:
        answer = False
        
    return answer