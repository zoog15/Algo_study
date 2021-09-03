x, y, w, h = map(int, input().split())

half_x = w/2
half_y = h/2

if x < half_x:
    x_d = x
else:
    x_d = w-x

if y < half_y:
    y_d = y
else:
    y_d = h-y

print(min(x_d,y_d))
