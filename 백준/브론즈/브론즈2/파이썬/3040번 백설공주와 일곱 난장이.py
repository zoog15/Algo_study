# 3040번 백설공주와 일곱 난장이 : https://www.acmicpc.net/problem/3040

a = []
one = 0
two = 0

for i in range(9):  # 9명의 모자숫자
    a.append(int(input()))

sum_s = sum(a)

for i in range(8):
    for j in range(i+1, 9):
        dif = (a[i] + a[j])
        if sum_s - dif == 100:
            one = a[i]
            two = a[j]

a.remove(one)
a.remove(two)

for i in a:
    print(i)
