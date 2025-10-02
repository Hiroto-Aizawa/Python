#n, k = map(int, input().split())
#a = list(map(int, input().split()))
data = input().split()

n = int(data[0])
k = int(data[1])
a = list(map(int, data[2:]))
print(a)
for i in range(len(a)):
    print(a[i])
# 初期ウィンドウの合計
# current_sum = sum(a[:k])
# max_sum = current_sum
# count = 1
# first_index = 0
# for i in range(k, n):
#     current_sum += a[i] - a[i - k]
#     if current_sum > max_sum:
#         max_sum = current_sum
#         count = 1
#         first_index = i - k + 1
#     elif current_sum == max_sum:
#         count += 1
# # 出力（1-indexed にするため +1）
# print(count, first_index + 1)

10