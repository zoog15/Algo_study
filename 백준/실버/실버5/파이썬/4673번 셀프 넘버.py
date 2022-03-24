# 1~10000까지의 숫자 들어가있는 리스트
numbers = []
# selfnum이 들어갈 set
s_num = set()

for i in range(1, 10001):
    numbers.append(i)
    # 각 자릿수로 나눈뒤 다시 int화 시켜서 i에 더하기
    for j in str(i):
        i += int(j)
    s_num.add(i)

answer = sorted(set(numbers) - s_num)

for i in answer:
    print(i)
