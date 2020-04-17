import math
N = int(input())
lmax = 0
point = [] # 空のリスト
for i in range(N):
    # appendでpointリストに追加
    point.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i != j: # 同じ点の比較は無用
            x1 = point[i][0]
            y1 = point[i][1]
            x2 = point[j][0]
            y2 = point[j][1]
            # 2点間の距離を求める
            l = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if lmax < l:
                lmax = l # lmax更新

print(lmax)