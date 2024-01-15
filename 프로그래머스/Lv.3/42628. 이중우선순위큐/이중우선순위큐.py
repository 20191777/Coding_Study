import heapq

def solution(operations):
    answer = []
    heap = []
    for oper in operations:
        if oper[0] == "I":
            heapq.heappush(heap, int(oper[2:]))
        elif oper[0] == "D" and oper[2:] == "1" and len(heap) > 0:
            heap.remove(max(heap))
        elif oper[0] == "D" and oper[2:] == "-1" and len(heap) > 0:
            heapq.heappop(heap)
        #print(heap)
    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer.append(max(heap))
        answer.append(heapq.heappop(heap))
    return answer