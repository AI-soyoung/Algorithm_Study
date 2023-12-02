from collections import defaultdict
while True:
    strs = input()
    if strs == '*': break

    flag = True
    for i in range(len(strs)-1):
        dicts = defaultdict(str)
        for j in range(len(strs)-1-i):
            s = strs[j] + strs[j+1+i]
            if s not in dicts:
                dicts[s] = '.'
            else: 
                flag = False
                break
        if flag == False: break

    if flag == False: print(f'{strs} is NOT surprising.')
    else: print(f'{strs} is surprising.')