n = int(input())
ns = set(map(int, input().split()))

m = int(input())
ms = list(map(int, input().split()))

for mm in ms:
    if mm in ns:
        print(1)
    else:
        print(0)