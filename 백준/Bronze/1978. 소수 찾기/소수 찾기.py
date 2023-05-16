import math

n = int(input())
nums = list(map(int, input().split()))
answer = 0

for num in nums:
    flag = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = 0
            break
    if num != 1 and flag == 1: answer += 1

print(answer)