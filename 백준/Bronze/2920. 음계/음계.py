scale = list(map(int, input().split()))

# sorted - 정렬 결과 리스트로 반환
if scale == sorted(scale):
    print("ascending")
elif scale == sorted(scale, reverse=True):
    print("descending")
else :
    print("mixed")