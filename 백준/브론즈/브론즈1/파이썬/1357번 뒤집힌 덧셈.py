def rev(x):
    rev_x = x[::-1]
    # print("뒤집힌 형태는",rev_x)
    int_x = int(rev_x)
    # print("정수 형태는",int_x)
    return int_x


a, b = map(str, input().split())

c = rev(a)+rev(b)

print(rev(str(c)))
