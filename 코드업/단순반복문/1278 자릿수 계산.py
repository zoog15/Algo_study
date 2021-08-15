n = int(input())
cnt = 0

while True:
    if n == 0:
        break
    n //= 10
    cnt += 1

print(cnt)