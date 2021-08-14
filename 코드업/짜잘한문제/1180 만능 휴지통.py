a = int(input())

ans = ((a%10*10) + a//10)*2

if ans>=100:
    ans -= 100

print(ans)
if ans <= 50:
    print("GOOD")
else:
    print("OH MY GOD")