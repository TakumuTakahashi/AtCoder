n = int(input())
# set型でユニークな値の要素数を取得すれば良い
d = len(set([int(input()) for _ in range(n)]))
print(d)