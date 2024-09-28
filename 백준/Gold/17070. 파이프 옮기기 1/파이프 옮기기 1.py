from collections import deque

N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))

# c_sts : 0 (가로) 1 (세로) 2 (대각선)
todo = deque()
todo.append([0, 0, 0])
result = 0

while todo:
    y, x, c_sts = todo.pop()

    if c_sts == 0:
        if y == N-1 and x == N-2:
            result += 1
            continue

        if x+2 < N and home[y][x+2] == 0:
            todo.append([y, x + 1, 0])
            if y+1 < N and home[y+1][x+1] == 0 and home[y+1][x+2] == 0:
                # 가로 2
                todo.append([y, x + 1, 2])

    elif c_sts == 1:
        if y == N-2 and x == N-1:
            result += 1
            continue

        if y+2 < N and home[y+2][x] == 0:
            todo.append([y + 1, x, 1])
            if x+1 < N and home[y+2][x+1] == 0 and home[y+1][x+1] == 0:
                # 세로 2
                todo.append([y + 1, x, 2])

    elif c_sts == 2:
        if y == N-2 and x == N-2:
            result += 1
            continue

        if x+2 < N and y+2 < N and home[y+1][x+2] == 0 and home[y+2][x+1] == 0 and home[y+2][x+2] == 0:
            # 대각선 3
            todo.append([y+1, x+1, 2])
        if x+1 < N and y+2 < N and home[y+2][x+1] == 0:
            # 대각선 2
            todo.append([y+1, x+1, 1])
        if x+2 < N and y+1 < N and home[y+1][x+2] == 0:
            # 대각선 1
            todo.append([y+1, x+1, 0])

print(result)