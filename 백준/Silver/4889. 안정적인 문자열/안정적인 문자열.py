idx = 0
while True:
    idx += 1
    answer = 0

    strs = input()
    if '-' in strs: break

    storage = list()
    score = 0
    for s in strs:
        if storage and s == '}' and storage[-1] == '{':
            storage.pop(-1)
        else:
            storage.append(s)
            
    for i in range(0, len(storage), 2):
        if storage[i] + storage[i+1] == '}{': answer += 2
        else: answer += 1
    print(f'{idx}. {answer}')