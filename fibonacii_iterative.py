n = int(input())
a, b = 1, 1
for i in range(n-1):
    a, b = b, a+b
print(a)

# things learnt
# fibonacci series numbering starts from 0th no
