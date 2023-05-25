def binary_search(cable_len: list, target_count: int):
    # 케이블 최대 길이 구하기

    # 케이블 길이가 될 수 있는 시작 길이:1 끝 길이:max
    start = 1
    end = max(cable_len)
    while start <= end:
        # 케이블 길이 중간값
        mid = (start + end) // 2
        cable_count = [(i // mid) for i in cable_len]
        # 길이를 더 짧게해서 개수를 늘려야하니까
        if sum(cable_count) < target_count: # 타켓 값이 최소 케이블 개수
            end = mid - 1
        # 길이를 더 길게해서 개수를 줄여도 되니까
        elif sum(cable_count) >= target_count:
            start = mid + 1
    print(end)


cable_num, target_count = map(int, input().split())

cable_len = [int(input()) for _ in range(cable_num)]

binary_search(cable_len, target_count)