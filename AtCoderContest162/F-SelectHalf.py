# 誤答
import math

N = int(input())
A = list(map(int, input().split()))
x = math.floor(N/2)

count = 0
for i in range(x):
    count += int(A[-(1+(2*i))])
print(count)