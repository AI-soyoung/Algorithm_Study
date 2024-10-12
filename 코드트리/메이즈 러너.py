import copy
from collections import defaultdict

def inRange(r, c):
    return 0 <= r < N and 0 <= c < N

def get_d(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

def p_move(er, ec):
    total_distance = 0
    del_p = list()
    for p, rcd in people.items():
        r, c, d = rcd
        nd = get_d(r, c, er, ec)
        if nd == 0: del_p.append(p)
        else:
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if inRange(nr, nc) and maps[nr][nc] <= 0:
                    if get_d(nr, nc, er, ec) < nd:
                        if nr == er and nc == ec:
                            del_p.append(p)

                        else:
                            people[p] = [nr, nc, d+1]
                        break
    for p in del_p:
        total_distance += people[p][2]+1
        del people[p]

    return people, total_distance

def m_rotate(er, ec):
    for l in range(2, N):
        for i in range(er-l+1, er+1):
            for j in range(ec-l+1, ec+1):
                if not inRange(i, j): continue
                for p, rcd in people.items():
                    pr, pc, pd = rcd
                    if i <= pr < i+l and j <= pc < j+l:
                        min_l = l
                        # 가장 작은 정사각형 잡음 -> 미로 회전, 참가자 회전, 출구 회전..
                        temp = list(m[j:j + l] for m in maps[i:i + l])
                        temp2 = [[0 for _ in range(l)] for _ in range(l)]
                        for tr in range(l):
                            for tc in range(l):
                                temp2[tc][l - tr - 1] = temp[tr][tc]

                        for tr in range(l):
                            for tc in range(l):
                                if temp2[tr][tc] > 0: temp2[tr][tc] -= 1
                                if temp2[tr][tc] == -1: er, ec = i + tr, j + tc
                                maps[i + tr][j + tc] = temp2[tr][tc]

                        for p2, rcd2 in people.items():
                            r2, c2, d2 = rcd2
                            if i <= r2 < i+l and j <= c2 < j+l:
                                # 사각형 안에 있으므로 회전시켜야 함
                                rr, cc = r2-i, c2-j
                                nr, nc = cc, l-rr-1
                                nr, nc = nr+i, nc+j
                                people[p2] = [nr, nc, d2]

                        return maps, er, ec, people


dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M, K = map(int, input().split())

maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))

people = defaultdict(list)
for idx in range(M):
    r, c = map(int, input().split())
    people[idx] = [r-1, c-1, 0]

r, c = map(int, input().split())
er, ec = r-1, c-1
maps[er][ec] = -1

result = 0

for _ in range(K):
    people, td = p_move(er, ec)

    result += td
    if not people: break
    
    maps, er, ec, people = m_rotate(er, ec)
    if not people: break

for p, rcd in people.items():
    result += rcd[2]
print(result)
print(er+1, ec+1)
