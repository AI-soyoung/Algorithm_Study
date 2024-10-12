from collections import defaultdict

def inRange(r, c):
    return 0 <= r < n and 0 <= c < n

def get_d(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

def move_thief():
    for idx, rcd in thiefs.items():
        r, c, d = rcd
        if get_d(cop[0], cop[1], r, c) <= 3:
            if not inRange(r+dr[d], c+dc[d]):
                if d == 0: d = 2
                elif d == 1: d = 3
                elif d == 2: d = 0
                elif d == 3: d = 1

            if r + dr[d] == cop[0] and c + dc[d] == cop[1]: r, c = r, c
            else: r, c = r + dr[d], c + dc[d]
            thiefs[idx] = [r, c, d]
    return thiefs

def move_cop(cop, type):
    r, c = cop

    # 달팽이 모양으로 움직임 / 반대 달팽이로 움직임
    if type :
        d = c_maps[r][c]
        nr, nc = r + dr[d], c + dc[d]
        cop = [nr, nc]
        nd = c_maps[nr][nc]
    else:
        d = r_c_maps[r][c]
        nr, nc = r + dr[d], c + dc[d]
        cop = [nr, nc]
        nd = r_c_maps[nr][nc]

    del_thief = list()

    for i in range(3):
        # 시야 체크
        if i > 0:
            nr, nc = nr + dr[nd], nc + dc[nd]
        if inRange(nr, nc):
            if tree_maps[nr][nc]: continue
            for t, rcd in thiefs.items():
                tr, tc, td = rcd
                if tr == nr and tc == nc:
                    del_thief.append(t)

    for t in del_thief:
        del thiefs[t]

    if cop[0] == 0 and cop[1] == 0: type = False
    elif cop[0] == n//2 and cop[1] == n//2: type = True

    return len(del_thief), cop, type

n, m, h, k = map(int, input().split())

# 달팽이 모양의 경찰 맵 만들기
cop = [n//2, n//2]
value = [0, 1, 2, 3]

v = 0
# directions = [0, 1, 2, 2, 3, 3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 0, 0, 0, 0, 0, ]
directions = list()
r_directions = list()
for i in range(n):
    for j in range(i+1):
        directions.append(value[v])
        r_directions.append(value[(v+2)%4])
    v = (v + 1) % 4
    for j in range(i+1):
        directions.append(value[v])
        r_directions.append(value[(v + 2) % 4])
    v = (v+1) % 4

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
start = [n//2, n//2]
c_maps = [[-1 for _ in range(n)] for _ in range(n)]
r_c_maps = [[-1 for _ in range(n)] for _ in range(n)]

c_maps[start[0]][start[1]] = 0
r_c_maps[start[0]][start[1]] = 0

for i, v in enumerate(directions):
    nr, nc = start[0]+dr[v], start[1]+dc[v]
    if 0 <= nr < n and 0 <= nc < n:
        c_maps[nr][nc] = directions[i+1]
        r_c_maps[nr][nc] = r_directions[i]
        start = [nr, nc]
    else: break

thiefs = defaultdict(list)
for idx in range(m):
    r, c, d = map(int, input().split())
    thiefs[idx] = [r-1, c-1, d]

tree_maps = [[False for _ in range(n)] for _ in range(n)]
for _ in range(h):
    r, c = map(int, input().split())
    tree_maps[r-1][c-1] = True

score = 0

type = True
for turn in range(1, k+1):

    thiefs = move_thief()

    num, cop, type = move_cop(cop, type)
    score += turn * num

    if not thiefs.keys(): break

print(score)
