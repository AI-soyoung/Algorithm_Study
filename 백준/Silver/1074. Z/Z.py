n, r, c = map(int, input().split())
z = 0

for i in range(1, n+1):
    st = 2 ** (n-i)
    if (r < st) & (c < st): 
        z += 0
    elif (r < st) & (st <= c < 2 * st):  
        z += st * st * 1
        c -= st
    elif (st <= r < 2 * st) & (c < st):  
        z += st * st * 2
        r -= st
    elif (st <= r < 2 * st) & (st <= c < 2 *st):  
        z += st * st * 3
        c -= st
        r -= st
print(z)