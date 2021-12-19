cut_x = [0]
cut_y = [0]

# 가로 세로 입력
x, y = map(int, input().split())
cut_x.append(y)
cut_y.append(x)

# 몇번 자를지 입력
cut = int(input())

# 0은 가로, 1은 세로
for i in range(cut):
    # 가로 혹은 세로, 지점
    dist, point = map(int,input().split())
    if dist == 0:
        cut_x.append(point)
    else:
        cut_y.append(point)

cut_x.sort()
cut_y.sort()

x_max = 0
y_max = 0
for i in range(len(cut_x)-1):
    len_x = cut_x[i+1] - cut_x[i]
    if len_x > x_max:
        x_max = len_x

for i in range(len(cut_y)-1):
    len_y = cut_y[i+1] - cut_y[i]
    if len_y > y_max:
        y_max = len_y

print(x_max * y_max)