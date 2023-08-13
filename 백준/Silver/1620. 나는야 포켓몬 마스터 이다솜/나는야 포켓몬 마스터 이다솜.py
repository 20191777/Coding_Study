import sys

input = sys.stdin.readline
n, m = map(int, input().split())

po_list = []
for i in range(n):
    po_list.append(input().rstrip())

for i in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(po_list[int(question)-1])
    else:
        print(po_list.index(question) + 1)
