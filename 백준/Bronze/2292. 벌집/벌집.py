n = int(input())

# 방이 6의 배수로 증가
num_hive = 1    # 1개 부터 시작
cnt = 1         # 방이 6배 씩 증가하는 횟수
while n > num_hive:
    num_hive += 6 * cnt
    cnt += 1

print(cnt)