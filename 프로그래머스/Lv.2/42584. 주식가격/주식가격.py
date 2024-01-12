from collections import deque

prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    prices = deque(prices)

    while len(prices) != 0:
        s = 0
        p = prices.popleft()
        for e in prices:
            s += 1
            if p > e:
                break
        answer.append(s)

    return answer

print(solution(prices))