i = 1


def asc_p(n):
    global i
    if i == n+1: return
    print(i)
    i += 1
    asc_p(n)


n = int(input())
asc_p(n)