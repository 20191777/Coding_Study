import sys

s = sys.stdin.readline().rstrip()

cnt = 0
for i in range(len(s)//2):
    if(s[i] == s[len(s)-i-1]):
        cnt += 1
    else:
        break
if(cnt == len(s)//2):
    print(1)
else:
    print(0)