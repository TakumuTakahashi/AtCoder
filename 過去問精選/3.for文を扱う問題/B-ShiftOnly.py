ans = 10**9 # anserの最大値は10の9乗
N =  int(input())
A = list(map(int, input().split()))
for i in A:
    p = 0
    while i % 2 == 0:
        i /= 2 # i = i/2 と同義
        p += 1
    if p < ans:
        ans = p
print(ans)