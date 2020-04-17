N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
    isum = sum(map(int, str(i)))
    if A <= isum <= B:
        ans += i
print(ans)