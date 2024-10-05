from collections import deque

box = list()
M, N = map(int, input().split())
for _ in range(N):
    box.append(list(map(int, input().split())))

visited = list()
cnt = 0
q = deque()
for r in range(N):
    for c in range(M):
        if box[r][c] == 1: q.append([r, c])

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
while q:
    tr, tc = q.popleft()
    for i in range(4):
        nr, nc = tr+dr[i], tc+dc[i]
        if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
            box[nr][nc] = box[tr][tc] + 1
            q.append([nr, nc])
max_d = 0
for b in box:
    if 0 in b:
        print(-1)
        exit()
    else:
        max_d = max(max(b), max_d)
print(max_d -1)