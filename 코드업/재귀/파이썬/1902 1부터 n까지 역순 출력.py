def des_p(n):
    print(n)
    n -= 1
    if n == 0: return
    des_p(n)


n = int(input())
des_p(n)