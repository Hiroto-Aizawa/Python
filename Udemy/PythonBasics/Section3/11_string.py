"""
11. 文字列
"""

# 文字列の出力は'', "" どちらでくくっても文字列と判定される
print('Hello')
# Hello
print("Hello")
# Hello

# '' と ""の使い分け
print("I don't know")
# I don't know
#print('I don't know')
# シングルクォートが奇数なので、終点が分からずSyntax Errorになる
print('I don\'t know')
# \でエスケープすることで文字列の指定用の'でないことを明示する

print('say "I don\'t know" ')
# say "I don't know"
print("say \"I don't know\"")

# 改行したい場合
print('Hello. \n How art you?')
# Hello
# How are you?

# rを文字列の前に置くことでrow dataであることを明示する
print(r'C:\name\name')
# C:\name\name

print('################')
print("""\
line1
line2
line3\
""")
print('################')
"""
################
line1
line2
line3
################
"""

# 演算子を使って文字列を連続して表示する
print('Hi.' * 3 + 'Mike.')
# Hi.Hi.Hi.Mike.

# 文字列の結合
print('Py' + 'thon')
# Python
prefix = 'Hello'
print(prefix + 'World')
# Hello World

s = 'aaaaaaaaaaaaaaaaaaaaaaaa' \
    'bbbbbbbbbbbbbbbbbbbbbbbb'

print(s)
# aaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbb