import sys
sys.setrecursionlimit(10**6)

def dfs(py, px):
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    xy[py][px] = 0
    for i in range(len(dx)):
        if py+dy[i] < 0 or px+dx[i] < 0 or py+dy[i] >= n or px+dx[i] >= m:
            continue
        if xy[py+dy[i]][px+dx[i]] != 0:
            dfs(py+dy[i], px+dx[i])
            
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    xy = [[0] * m for _ in range(n)] 

    for _ in range(k):
        x, y = map(int, input().split())
        xy[y][x] = 1
    
    bug = 0
    for y in range(n):
        for x in range(m):
            if xy[y][x] != 0:
                dfs(y, x)
                bug += 1

    print(bug)


