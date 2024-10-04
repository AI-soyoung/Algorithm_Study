from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answers = []
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx, 0))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[sy][sx] = True
    while q:
        y, x, cnt = q.popleft()
        flag = False
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] > 0 and not visited[ny][nx]:
                flag = True
                visited[ny][nx] = True
                q.append((ny, nx, cnt+1))
        if not flag:
            answers.append((cnt, grid[sy][sx]+grid[y][x]))
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            bfs(i, j)
answers.sort(key=lambda x:(x[0], x[1]), reverse=True)
print(answers[0][1])