import sys
from collections import deque

n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

# 상하좌우
startX = [-1, 1, 0, 0] 
startY = [0, 0, -1, 1]

def bfs(x, y):
    
    deq = deque()
    deq.append((x,y))

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            now_x = x + startX[i]
            now_y = y + startY[i]

            if 0 <= now_x < n and 0 <= now_y < m and maze[now_x][now_y] == 1:
                deq.append((now_x, now_y))
                maze[now_x][now_y] = maze[x][y] + 1
    
    return maze[n-1][m-1]

print(bfs(0,0))