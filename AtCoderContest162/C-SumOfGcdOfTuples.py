def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

K = int(input())
count = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            d = gcd(a,b)
            count += gcd(c, d)
print(count)