from collections import defaultdict, deque

def find_basecamp(i):
    dr, dc =  [-1, 0, 0, 1], [0, -1, 1, 0]
    sr, sc = s_list[i]

    # bfs 로 최단경로
    q = deque()
    q.append([sr, sc, 0])
    visited = deque()
    visited.append([sr, sc])
    min_r, min_c, min_d = n+1, n+1, 2*n+1
    while q:
        r, c, d = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and [nr, nc] not in visited and maps[nr][nc] >= 0:
                if maps[nr][nc] == 1 and d <= min_d:
                    if d < min_d:
                        min_d = d
                        min_r, min_c = nr, nc
                    elif d == min_d:
                        if min_r > nr:
                            min_r, min_c = nr, nc
                        elif min_r == nr:
                            if min_c > nc:
                                min_r, min_c = nr, nc
                    # return nr, nc
                q.append([nr, nc, d+1])
                visited.append([nr, nc])
    return min_r, min_c

def p_move():
    dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
    del_p = list()
    for p, rc in p_list.items():
        pr, pc = rc[0], rc[1]
        sr, sc = s_list[p][0], s_list[p][1]

        q = deque()
        q.append([pr, pc, []])
        visited = deque()
        visited.append([pr, pc])
        final_route = []
        flag = False
        while q:
            r, c, route = q.popleft()
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < n and 0 <= nc < n and [nr, nc] not in visited and maps[nr][nc] >= 0:
                    if nr == sr and nc == sc:
                        final_route = route
                        flag = True
                        break
                    q.append([nr, nc, route+[[nr, nc]]])
                    visited.append([nr, nc])
            if flag: break

        if flag:
            if not final_route:
                # 편의점 도착
                p_list[p] = [sr, sc]
                del_p.append(p)
            else:
                p_list[p] = final_route[0]

    for p in del_p:
        sr, sc = p_list[p]
        maps[sr][sc] = -1
        del p_list[p]


n, m = map(int, input().split())
maps = list()
for _ in range(n):
    maps.append(list(map(int, input().split())))


# 편의점 좌표
s_list = defaultdict(list)
for idx in range(1, m+1):
    sr, sc = map(int, input().split())
    # maps[sx][sy] = idx
    s_list[idx] = [sr-1, sc-1]

# 사람 좌표
p_list = defaultdict(list)
t = 1
while True:
    if t >= 2 and not p_list:
        print(t-1)
        break

    p_move()

    if t <= m:
        pr, pc = find_basecamp(t)
        p_list[t] = [pr, pc]
        maps[pr][pc] = -1
    t += 1

