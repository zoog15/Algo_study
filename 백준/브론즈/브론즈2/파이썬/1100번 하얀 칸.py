chess = [[0] * 8 for _ in range(8)]

for i in range(8):
    chess[i] = input()

white_cnt = 0  # 하얀 말의 갯수

for i in range(8):
    for j in range(8):
        # 홀수행, 0,2,4,6이 하얀칸
        if i%2 == 0:
            if j%2 == 0 and chess[i][j] == 'F':
                white_cnt += 1
        # 짝수행, 1,3,5,7이 하얀칸
        else:
            if j%2 == 1 and chess[i][j] == 'F':
                white_cnt += 1

print(white_cnt)