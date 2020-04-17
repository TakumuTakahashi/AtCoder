n, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
count = 0
for i in range(n):
    if A[i] <= x:
        count += 1
        x -= A[i]
print(count)