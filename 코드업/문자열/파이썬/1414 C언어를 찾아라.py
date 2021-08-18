s = input();

a = s.upper()

cnt1 = 0
cnt2 = 0

for i in a:
    if i == 'C':
        cnt1 += 1

for i in range(len(a)-1):
    if a[i] == 'C' and a[i+1] == 'C':
        cnt2 += 1

print(cnt1)
print(cnt2)