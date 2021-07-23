a = []
one = 0
two = 0

for i in range(9):  # 9명의 키 입력받기
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

a.sort()

for i in a:
    print(i)
