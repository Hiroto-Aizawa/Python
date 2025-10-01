# https://paiza.jp/works/mondai/class_primer/class_primer__make?language_uid=python3

import textwrap

n = int(input())

for i in range(n):
    s = input().split()

    user_data = textwrap.dedent(f"""\
    User{{
    nickname : {s[0]}
    old      : {s[1]}
    birth    : {s[2]}
    state    : {s[3]}
    }}""")

    print(user_data)