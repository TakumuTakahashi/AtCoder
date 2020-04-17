n, l = map(int, input().split())
# リスト内包表記
# 以下と同等
## strs = []
## for i in range(n):
##    strs.append(input())
strs = [input() for _ in range(n)]
strs.sort()
strs = ''.join(strs)
print(strs)