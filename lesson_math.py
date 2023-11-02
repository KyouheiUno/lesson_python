import math


# 円の面積を求めるメソッドを定義する

def calculation_circle_area(radius):
    answer = radius * radius * math.pi
    print('演習率は{}です。そして設定された半径は{}でした'.format(answer, radius))
    print(answer)


# 半径は5に設定
radius = 5
# 円の面積を求める処理を実行
calculation_circle_area(radius)
