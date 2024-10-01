import copy
from collections import deque

def rotate(r, c, d):
    # 회전에 따라 값 변경하기
    temp = copy.deepcopy(umul)
    if d == 90:
        temp[r-1][c-1] = umul[r+1][c-1]
        temp[r-1][c] = umul[r][c-1]
        temp[r-1][c+1] = umul[r-1][c-1]

        temp[r][c+1] = umul[r-1][c]

        temp[r+1][c+1] = umul[r-1][c+1]
        temp[r+1][c] = umul[r][c+1]
        temp[r+1][c-1] = umul[r+1][c+1]

        temp[r][c-1] = umul[r+1][c]
    elif d == 180:
        temp[r - 1][c - 1] = umul[r + 1][c + 1]
        temp[r - 1][c] = umul[r+1][c]
        temp[r - 1][c + 1] = umul[r + 1][c - 1]

        temp[r][c + 1] = umul[r][c-1]

        temp[r + 1][c + 1] = umul[r - 1][c - 1]
        temp[r + 1][c] = umul[r-1][c]
        temp[r + 1][c - 1] = umul[r - 1][c + 1]

        temp[r][c - 1] = umul[r][c+1]

    elif d == 270:
        temp[r - 1][c - 1] = umul[r - 1][c + 1]
        temp[r - 1][c] = umul[r][c+1]
        temp[r - 1][c + 1] = umul[r + 1][c + 1]

        temp[r][c + 1] = umul[r+1][c]

        temp[r + 1][c + 1] = umul[r+ 1][c - 1]
        temp[r + 1][c] = umul[r][c-1]
        temp[r + 1][c - 1] = umul[r - 1][c - 1]

        temp[r][c - 1] = umul[r-1][c]
    return temp

def get_value(temp):
    # 최대 유물 획득가치 찾기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    todo = deque()
    visited = deque()
    result = 0
    t_del = list()

    for tr in range(5):
        for tc in range(5):
            todo.append([tr, tc])
            num_v = 1
            temp_delete = list()
            v = temp[tr][tc]

            while todo:
                r, c = todo.pop()

                if temp[r][c] == v and [r, c] not in visited:
                    visited.append([r, c])

                    for i in range(4):
                        if r + dx[i] < 0 or c + dy[i] < 0 or r + dx[i] > 4 or c + dy[i] > 4:
                            continue
                        if temp[r + dx[i]][c + dy[i]] == v and [r+dx[i], c+dy[i]] not in visited:
                            todo.append([r + dx[i], c + dy[i]])
                            if [r+dx[i], c+dy[i]] not in temp_delete:
                                temp_delete.append(([r+dx[i], c+dy[i]]))
                                num_v += 1
            if num_v >= 3:
                result += num_v
                t_del.extend(temp_delete)
                t_del.append([tr, tc])

            temp_delete.clear()
    return result, t_del

def rotate_get(umul):
    # 회전하면서 새로운 유물지도 그리기
    r_value = -1
    r_c, r_r, r_d = 5, 5, 360
    r_del = list()

    for i in range(1, 4):
        for j in range(1, 4):
            for d in [90, 180, 270]:
                temp = rotate(i, j, d)
                t_value, t_del = get_value(temp)
                # 최대값으로 업데이트
                flag = False
                if r_value < t_value:
                    flag = True
                elif r_value == t_value:
                    if r_d > d:
                        flag = True
                    elif r_d == d:
                        flag = False
                        if r_c > j:
                            flag = True
                        elif r_c == j:
                            flag = False
                            if r_r > i: flag = True
                if flag == True:
                    r_value, r_r, r_c, r_d, r_del, r_umul = t_value, i, j, d, t_del, temp

    return r_value, r_r, r_c, r_d, r_del, r_umul

def fill_umul(r_del, new_v, umul):
    r_del.sort(key=lambda x: (x[1], -x[0]))

    for dr, dc in r_del:
        v = new_v.popleft()
        umul[dr][dc] = v
    return umul

if __name__ == '__main__':

    k, m = map(int, input().split())
    umul = list()
    for _ in range(5):
        umul.append(input().split())
    new_v = deque(input().split())

    final_result = list()
    for _ in range(k):
        total = 0
        # 유적 회전하고 최대 유적 상태 찾기
        r_value, r_r, r_c, r_d, r_del, umul = rotate_get(umul)

        if r_value == 0: break
        # 최대 유적 개수를 토탈에 더하기
        total += r_value

        while r_value > 0:
            # 새로운 값으로 유적 채우기
            umul = fill_umul(r_del, new_v, umul)
            # 최대 유적 개수 찾기, 지워야할 부분 찾기
            r_value, r_del = get_value(umul)
            total += r_value
        if total != 0:
            final_result.append(total)

    print(*final_result)
