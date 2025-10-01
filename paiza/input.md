# 標準入力について

## 1行1列の入力を受け取る場合
【入力】  
N

```python
# 文字列を受け取る場合
s = input()

# 整数を受け取る場合
n = int(input())

# 少数を受け取る場合
f = float(input())
```

## 1行複数列の入力を受け取る場合
【2つの入力】  
A B(2つの文字列)

【3つの入力】  
X Y Z(3つの整数)

【3つの入力】  
H M S(3つの小数)

```python
# 文字列を受け取る場合
A, B = input().split()

# 整数を受け取る場合
X, Y, Z = map(int, input().split())

# 小数を受け取る場合
H, M, S = map(float, input().split())
```

## カンマ区切り文字列を受け取る場合

```python
# 文字列を受け取る場合
A, B, C = input().split(",")

# 可変長の文字列を受け取る場合
S = input().split(",")
for i in range(len(S)):
    print(str[i])
```

## 1行の配列を受け取る場合
【入力】  
A1 A2 A3 ... AN

```python
# 文字列を受け取る場合
A = input().split()
for S in A:
    print(S)

# 整数列を受け取る場合
A = list(map(int, input().split()))

# 小数列を受け取る場合
A = list(map(float, input().split()))
```

## 複数行複数列の入力を受け取る場合

【入力】  
A1,1 A1,2 A1,3 ... A1,N  
A2,1 A2,2 A2,3 ... A2,N  
...  
AN,1 AN,2 AN,3 ... AN,N  

以下の例は、`内包表記`を使用しています
```python
N = int(input())
# 複数行の文字列を受け取る場合
A = [input().split() for _ in range(N)]

# 複数行の整数列を受け取る場合
A = [list(map(int, input().split())) for _ in range(N)]

# 複数行の小数列を受け取る場合
A = [list(map(float, input().split())) for _ in range(N)]
```