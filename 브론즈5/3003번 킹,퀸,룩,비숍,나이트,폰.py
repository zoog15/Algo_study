a = [1, 1, 2, 2, 2, 8]  # 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
b = list(map(int, input().split()))  # 흰색 킹,퀸,룩,비숍,나이트,폰 갯수 입력

c = len(b)

for i in range(0, c):
    dif = a[i] - b[i]
    print(dif, end=' ')
