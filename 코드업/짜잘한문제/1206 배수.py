a, b = map(int, input().split())

if b % a == 0:
    print(f'{a}*{int(b/a)}={b}')
elif a % b == 0:
    print(f'{b}*{int(a/b)}={a}')
else:
    print("none")