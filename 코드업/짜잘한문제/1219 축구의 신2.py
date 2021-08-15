a, b, c = map(int, input().split())

sc = (89-a)//5 +1

if b+sc > c:
    print("win")
elif b+sc == c:
    print("same")
else:
    print("lose")

