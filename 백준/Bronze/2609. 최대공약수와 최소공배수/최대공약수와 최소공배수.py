n, m = map(int, input().split())

i = min(n, m)
while True:
    if n % i == 0 and m % i == 0: break
    else: i -= 1

print(i)
print(i * (n//i) * (m//i))