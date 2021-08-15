def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a-1)


n = int(input())
print(fact(n))