import sys
input = sys.stdin.readline
n = int(input())

stack = list(map(int, input().rstrip().split()))
wait = []

cnt = 1
def dokidoki():
    cnt = 1
    while stack or wait:
        #print("stack :", stack)
        #print("wait :", wait)

        if wait and wait[-1] == cnt:
            wait.pop()
            cnt += 1

        elif stack and stack[0] != cnt:
            wait.append(stack.pop(0))

        elif stack and stack[0] == cnt:
            stack.pop(0)
            cnt += 1

        elif len(stack) == 0 and wait and wait[-1] != cnt:
            print("Sad")
            return

        elif stack and stack[0] != cnt:
            wait.append(stack.pop(0))
    print("Nice")
dokidoki()
