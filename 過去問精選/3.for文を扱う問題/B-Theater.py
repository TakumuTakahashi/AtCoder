N = int(input())
# 変数名を"_"にすることで「その変数を使っていません」ということを表現している(Pythonの習慣)
# リストの中にリスト
box = [list(map(int, input().split())) for _ in range(N)]
sum = 0
for i in range(N):
    # 各リストの人数を求める
    sum += box[i][-1] - box[i][0] + 1
print(sum)