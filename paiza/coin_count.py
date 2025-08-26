"""
入力された金額を 500円、100円、50円、10円、5円、1円硬貨 を使って
最小枚数 に分解し、硬貨の合計枚数を出力する
"""

amount = int(input())

coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)
