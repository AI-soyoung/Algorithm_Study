from collections import deque
S = input()
P = deque(input())

answer = 0

temp = deque()
while P:
    temp.append(P.popleft())
    flag = False

    for i in range(len(S)-len(temp)+1):
        if S[i:i+len(temp)] == ''.join(temp): 
            flag = True
            break
    
    if flag == False: 
        P.appendleft(temp[-1])
        temp = deque()
        answer += 1

answer += 1
print(answer)