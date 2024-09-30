def solution(want, number, discount):
    answer = 0
    target_d = dict()
    window_d = dict()
    
    for i, w in enumerate(want):
        target_d[w] = number[i]
        window_d[w] = 0
    
    # 초기 window 세팅
    for i in range(10):
        if discount[i] in target_d.keys():
            window_d[discount[i]] += 1
    
    # sliding window 
    for idx in range(len(discount) - 10+1):
        # print(window_d)
        flag = 0
        for i in target_d:
            if target_d[i] > window_d[i]: 
                flag = 1 
                break
        
        if flag == 0: answer += 1
        
        if discount[idx] in target_d.keys():
            window_d[discount[idx]] -= 1
            
        if idx + 10 < len(discount) and discount[idx + 10] in target_d.keys():
            window_d[discount[idx+10]] += 1
        
    return answer