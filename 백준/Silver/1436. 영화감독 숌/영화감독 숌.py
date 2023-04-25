n = int(input())
cnt = 0
n_th = 666
while True:
    if '666' in str(n_th):
        cnt += 1
    if cnt == n:
        print(n_th)
        break
    n_th += 1