s = input()
for i in range(len(s)):
    # s[0]から開始するため奇数番目の文字のインデックスは2で割り切れる
    if i%2 == 0:
        # end = ''で改行なしの標準出力
        print(s[i], end = '')