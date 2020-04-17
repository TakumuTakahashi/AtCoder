n = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()
ans = 0
for i in range(n):
    ans += A[1 + 2*i]
print(ans)