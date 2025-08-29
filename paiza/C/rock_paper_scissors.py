# https://paiza.jp/works/challenges/710/retry

n = int(input())
ans = 0

for _ in range(n):
    alice, bob = map(str, input().split())
    if alice == "G" and bob == "C":
        ans += 1
    elif alice == "C" and bob == "P":
        ans += 1
    elif alice == "P" and bob == "G":
        ans += 1
    else:
        pass
print(ans)