#スペース区切りの整数を入力しリストにいれる
rgb_list = list(map(int, input().split()))
rgb_list = map(str, rgb_list) # join関数は文字列の結合をするからmap関数で型変換
rgb = ''.join(rgb_list) # リストの中身を連結
# 4で割り切れるか
if int(rgb) % 4 == 0: # int型に戻す
    print('YES')
else:
    print('NO')

#---別解---
#r,g,b = map(int, input().split())
#if (10*g + b) % 4 == 0:
    # 以下略