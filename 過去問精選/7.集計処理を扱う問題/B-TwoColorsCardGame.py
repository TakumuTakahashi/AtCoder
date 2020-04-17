N = int(input())
st = set() # 空のセットを生成
s = [] # 空のリストを生成

for i in range(N):
    char = input()
    st.add(char) # セットに要素を追加するにはadd()を使う
    s.append(char) # リストに要素を追加するにはappend()を使う

M = int(input())
t = [] # 空のリストを生成

for i in range(M):
    t.append(input())

ans = -100 # ありうる最小値を初期値に設定
char = 0

for x in st:
    char = s.count(x)
    char -= t.count(x)
    ans = max(ans, char)

print(ans if 0 <= ans else 0)