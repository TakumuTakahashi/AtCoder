N, M = map(int, input().split())
# 任意の値、要素数で初期化
l = [0] * N
for i in range(M):
    # 1 2 が入力されたらリストの 0と1 をインクリメントする
    a, b = [int(x) - 1 for x in input().split()]
    l[a] += 1
    l[b] += 1

for i in range(N):
    print(l[i])