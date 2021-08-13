n = input()
a = int(n,16)

for i in range(1, 16):
    print('%X'%a, '*%X'%i, '=%X'%(a*i), sep='')