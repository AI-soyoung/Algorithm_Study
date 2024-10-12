import copy
from collections import deque

TC = int(input())
for t in range(1, TC+1):
    nums, exchange = input().split()

    max_result = 0
    set_result = set()
    set_result.add(nums)

    for i in range(int(exchange)):
        set_temp = set()
        for r_num in set_result:
            n = list()
            for r in str(r_num):
                n.append(r)


            for j in range(len(n)):
                for k in range(len(n)):
                    if j == k : continue
                    temp = copy.deepcopy(n)
                    temp[j], temp[k] = temp[k], temp[j]
                    result = int(''.join(temp))
                    set_temp.add(result)
        set_result = set_temp
    print(f'#{t} {max(set_result)}')


