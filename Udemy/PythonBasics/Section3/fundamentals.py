"""
8.変数宣言
"""
print('Hi')

num = 1
name = '1'

# 文字列 -> int へのキャスト
new_num = int(num)
# 変数の型を確認する
print(new_num, type(new_num))


"""
9.まずはprintで出力
"""

print('Hi', 'Mike')
# Hi Mike

# sep: 文字列と文字列の区切りを指定
# end: 文末の指定（改行など）
print('Hi', 'Mike', sep=',', end='.\n')
# Hi,Mike.
#

"""
10. 数値
"""

50 - 5 * 6
# 20

(50 - 5) * 6
# 270

8 / 5
# 1.6

type(1)
# <class int>

type(1.6)
# <class float>

# 除算
17 / 3
# 5.666666666666667

# 除算　整数のみ
17 // 3
# 5

# 除算の余り
17 % 3
#　2

5 * 5
# 25

# べき乗
5 ** 2
# 25

5 ** 5
# 3125

# 小数の丸め
pi = 3.141592653589793
round(pi, 2)
# 3.14

# 数学関数のインポート
import math

print(help(math))