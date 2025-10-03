"""
12 文字列のインデックスとスライス
"""

word = 'python'
print(word[0])
# p
print(word[1])
# y
print(word[-1])
# n 最後のインデックスを指定

print(word[0:2])
# py 0から2までのインデックスの内容を出力
print(word[2:5])
# tho　2から5までのインデックスの内容を出力
print('################')
print(word[0:2])
print(word[:2])
# py　どちらも0から2までのインデックスを指定する
print('################')
print(word[2:])
# thon 2から最後のインデックスまで指定
print('################')

# 最初の文字をjにしてpython から jythonに変更する
word = 'j' + word[1:]
print(word[:])
# jython 最初から最後のインデックスを指定

n = len(word)
print(n)
# 6