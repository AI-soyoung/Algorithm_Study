import sys
t = int(sys.stdin.readline())
test = []
for i in range(t):
    test.append(int(sys.stdin.readline()))

for c in test:
    x1 = [1, 0]
    x2 = [0, 1]

    if c == 0: print(x1[0], x1[1])
    elif c == 1: print(x2[0], x2[1])
    else:
        for i in range(c-1):
            temp = [x1[0] + x2[0], x1[1] + x2[1]]
            x1 = x2
            x2 = temp
        print(temp[0], temp[1])