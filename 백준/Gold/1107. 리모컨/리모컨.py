btn = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

n = int(input())
m = int(input())
if m != 0: 
    btn = btn - set(input().split())

min_cnt = abs(100 - n)
for i in range(1000000):
    num = str(i)

    for j in range(len(num)):
        if num[j] not in btn:
            break
        elif j == len(num) -1:
            min_cnt = min(min_cnt, abs(int(num) - n) + len(num))
print(min_cnt)
