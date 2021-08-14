a = input()

if a == '11' or a == '12' or a == '13':
    print(a+'th')
elif int(a) % 10 == 1:
    print(a+'st')
elif int(a) % 10 == 2:
    print(a+'nd')
elif int(a) % 10 == 3:
    print(a+'rd')
else:
    print(a+'th')