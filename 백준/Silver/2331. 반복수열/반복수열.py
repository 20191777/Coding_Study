# 수열의 수 계산
def cal_sequence(a, p):
    answer = 0
    for i in str(a):
        answer += pow(int(i), p)
    return answer

def dfs(a, p, count, check):
    # 해당 수열 값이 중복된 지 확인
    # 중복된 수라면 이미 그 자리엔 개수가 있기 때문
    if check[a] != 0:
        return check[a] - 1

    check[a] = count
    next = cal_sequence(a, p)
    count += 1
    
    # 중복이 생길 때 까지 탐색
    return dfs(next, p, count, check)


# 각 index는 수열의 수를 뜻함
check = [0]*250000  # 최댓값 4*9^5
    
# 첫수, 제곱 횟수
a, p = map(int, input().split())
count = 1   # 나온 수열의 개수
print(dfs(a, p, count, check))