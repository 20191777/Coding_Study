from collections import deque

def solution(arr):
    d = deque(arr)
    answer = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            d.popleft()
        else:
            answer.append(d.popleft())

        if i == len(arr)-2:
            answer.append(d.popleft())
    return answer