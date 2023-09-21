import sys

def solve(idx, result, add, subtract, multiply, divide):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if add > 0:
        # print(1)
        solve(idx + 1, result + numbers[idx], add - 1, subtract, multiply, divide)
    if subtract > 0:
        # print(2)
        solve(idx + 1, result - numbers[idx], add, subtract - 1, multiply, divide)
    if multiply > 0:
        # print(3)
        solve(idx + 1, result * numbers[idx], add, subtract, multiply - 1, divide)
    if divide > 0:
        # print(4)
        if result >= 0:
            solve(idx + 1, result // numbers[idx], add, subtract, multiply, divide - 1)
        else:
            solve(idx + 1, -(-result // numbers[idx]), add, subtract, multiply, divide - 1)

N = int(input())
numbers = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

max_result = float('-inf')
min_result = float('inf')

solve(1, numbers[0], add, subtract, multiply, divide)

print(max_result)
print(min_result)