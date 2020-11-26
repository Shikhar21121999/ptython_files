
n = int(input())
ans = 2
for x in range(2, n):
    ans *= x
print(ans//n)
