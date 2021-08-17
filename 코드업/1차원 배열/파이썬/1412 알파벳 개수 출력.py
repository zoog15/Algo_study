a = [0 for _ in range(26)]

s = input()

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        a[ord(s[i])-ord('a')] += 1
    else:
        continue

for i in range(len(a)):
    print(f'{chr(i+ord("a"))}:{a[i]}')
