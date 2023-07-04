n = 10
p = 5
t = 15

if p > n and n > t:
    print(p, n, t)
elif n > p and p > t:
    print(n, p, t)
elif t > n and n > p:
    print(t, n, p)
elif p > t and t > n:
    print(p, t, n)
elif n > t and t > p:
    print(n, t, p)
else:
    print(t, p, n)
