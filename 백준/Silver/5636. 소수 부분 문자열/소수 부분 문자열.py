# 5636 - 소수 부분 문자열
import math

max_n = 100000
array = [True for i in range(max_n+1)]
for i in range(2, int(math.sqrt(max_n)) + 1):
    if array[i] == True: 
        j = 2
        while i * j <= max_n:
            array[i*j] = False
            j += 1

while True:
    num = input()
    if num == '0': break
    
    sets = set()
    for gap in range(min(len(num), 5)):
        for idx in range(len(num)-gap):
            n = int(num[idx:idx+gap+1])
            sets.add(n)

    max_p = 0

    for s in sets:
        if array[s] == True:
            max_p = max(max_p, s)
    print(max_p)