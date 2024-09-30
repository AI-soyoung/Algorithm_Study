from itertools import permutations
def solution(k, dungeons):
    # mnp 최소 필요 피로도 : 던전 탐험 시작에 필요함
    # hp 소모 피로도 : 던전 탐험 마치고 소모됨
    
    # 현재 피로도 k
    # 각 던전별 최소 필요 피로도와 소모 피로도가 담긴 2차원 배열 dungeons
    # 유저가 탐험할 수 있는 최대 던전 수
    
    answer = []
    
    route = list(permutations(dungeons, len(dungeons)))
    # print(route)
    
    for r in route:
        temp = 0
        temp_k = k
        for mnp, hp in r:
            if temp_k >= mnp: 
                temp_k -= hp
                temp += 1
            else: 
                break
        answer.append(temp)
    print(answer)
    return max(answer)