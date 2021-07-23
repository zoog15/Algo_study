total = 0
a = []  # 각 역에서의 인원을 저장하기위한 배열

for i in range(10):
    p, q = map(int, input().split())
    total -= p  # p만큼 내림
    total += q  # p만큼 탑승
    a.append(total)

total = a[0]  # 첫번째 값 넣어주기

for i in range(10):
    if a[i] > total:
        total = a[i]

print(total)
