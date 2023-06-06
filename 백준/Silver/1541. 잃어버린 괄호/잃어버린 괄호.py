exp = input().split('-')
result = 0

for i, e in enumerate(exp):
    temp = 0
    tmp = map(int, e.split('+'))
    temp += sum(tmp)
    if i == 0:
        result += temp
    else:
        result -= temp
print(result)