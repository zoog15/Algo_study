n = int(input())

a = list(map(int, input().split()))

for i in range(len(a)):
    print(f'{i + 1}:', end=' ')
    for j in range(len(a)):
        if j == i: continue
        if a[i] < a[j]:
            print("<", end=' ')
        elif a[i] > a[j]:
            print(">", end=' ')
        else:
            print("=", end=' ')
    print()