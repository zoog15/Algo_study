def odd_p(a, b):
    if a == b+1: return
    if a%2 == 1:
        print(a, end=' ')
    a += 1
    odd_p(a,b)


a, b = map(int, input().split())
odd_p(a, b)