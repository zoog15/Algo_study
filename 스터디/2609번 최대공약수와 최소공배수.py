p, q = map(int, input().split())
gcf = 0  # 최대공약수
lcm = 0  # 최소공배수

if q > p:
    temp = p
    p = q
    q = temp

cen_n = q // 2

if p % q == 0:  # 큰수가 작은수로 나누어떨어지면 최대공약수는 작은수, 최소공배수는 큰 수
    gcf = q
    lcm = p
else:
    for i in range(1, cen_n+1):  # 더 작은 수의 중간값보다 큰 수들은 최대공약수가 될 수 없음
        if p % i == 0 and q % i == 0:
            gcf = i
    for j in range(1, p+1):
        if (p*j) % q == 0:
            lcm = (p*j)
            break

print(gcf)
print(lcm)
