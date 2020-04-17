N = int(input())
ans = 1000000
for i in range(1, N+1):
    A = i
    B = N - i
    if A <= B: # A>Bの計算は無意味
        Asum = sum(map(int, str(A)))
        Bsum = sum(map(int, str(B)))
        if ans > (Asum + Bsum):
            ans = Asum + Bsum
print(ans)