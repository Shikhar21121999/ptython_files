Mod = 998244353
n = int(input())
a, b = 1, 1
# find nth fibnumber
for i in range(n-1):
    a, b = b, a+b
print(a*pow(1 << n, Mod-2, Mod) % Mod)

# things learnt
# fibonacci series numbering starts from 0th no
# in python we can directly use pow to implement modulo
# when we have to find modulo fraction of a number we use little fermats formula when mod is a prime number
