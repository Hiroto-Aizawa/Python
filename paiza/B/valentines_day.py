# https://paiza.jp/career/challenges/666/retry

N, H, M = map(int, input().split())
sy, sx = map(int, input().split())
move = input()
grid = [list(map(int, input().split())) for  _ in range(H)]

# 配列の要素は0から始まるので-1しておく
sy -= 1
sx -= 1

for i in range(N):
    if move[i] == "F":
        sy -= 1
    elif move[i] == "R":
        sx += 1
    elif move[i] == "B":
        sy += 1
    elif move[i] == "L":
        sx -= 1

    print(grid[sy][sx])