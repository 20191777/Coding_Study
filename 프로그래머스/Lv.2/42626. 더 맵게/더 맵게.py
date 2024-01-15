import heapq
def solution(scoville, K):
    answer = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)

    m = heapq.heappop(heap)
    while m < K:
        if len(heap) == 0:
            answer = -1
            break
        new = m + heapq.heappop(heap) * 2
        heapq.heappush(heap, new)
        answer += 1
        m = heapq.heappop(heap)
    # print(scoville)
    return answer