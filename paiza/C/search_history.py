# https://paiza.jp/works/mondai/c_rank_skillcheck_archive/search_history

N = int(input())
history = []

for _ in range(N):
    word = input()
    if word in history:
        history.remove(word)  # 既にある場合は削除
    history.insert(0, word)   # 先頭に追加

for word in history:
    print(word)