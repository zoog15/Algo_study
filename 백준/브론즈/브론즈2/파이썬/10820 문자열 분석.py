import sys


def check(string):
    l, u, d, e = 0,0,0,0
    for i in string:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
        elif i.isdigit():
            d += 1
        else:
            e += 1

    print(l,u,d,e)


while True:
    string = sys.stdin.readline().rstrip("\n")
    if not string:
        break

    check(string)
