for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    db = [-2, -1, 1, 2]
    result = 0
    for i, b in enumerate(buildings):
        max_height = 0
        for j in range(4):
            if buildings[i+db[j]] >= b:
                # 조망권 없음
                max_height = b
                break
            else:
                # 조망권 있음. 몇 세대나 가려지지?
                if buildings[i+db[j]] > max_height:
                    max_height = buildings[i+db[j]]
        result += (b - max_height)

    print(f'#{tc} {result}')
