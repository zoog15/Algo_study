a = int(input())

if a%400 == 0 or (a%4 == 0 and a%100 != 0):
    print("yes")
else:
    print("no")