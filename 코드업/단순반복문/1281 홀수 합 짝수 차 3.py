a, b = map(int, input().split())
sum = 0
cnt = 0

for i in range(a, b+1):
    if i % 2 == 1:
        if cnt == 0:
            print(i, end='')
            cnt += 1
        else:
            print(f'+{i}', end='')
        sum += i
    else:
        print(f'-{i}', end='')
        sum -= i
        cnt += 1

print(f'={sum}')