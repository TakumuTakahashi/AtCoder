n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
# slice操作 --> [start:stop:step]
# 奇数番目の要素の和 - 偶数番目の要素の和
print(sum(a[::2]) - sum(a[1::2]))