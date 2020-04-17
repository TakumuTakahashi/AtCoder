s = list(input())
t = list(input())
s.sort() # list.sort()で昇順にソート
t.sort()
t.reverse() # ソートした文字列を逆順に並び替え
s = ''.join(s)
t = ''.join(t)
if s < t:
    print('Yes')
else:
    print('No')