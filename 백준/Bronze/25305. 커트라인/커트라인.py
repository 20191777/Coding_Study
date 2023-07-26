n, k = map(int, input().split())
points = list(map(int, input().split()))

points.sort()

print(points[n-k])