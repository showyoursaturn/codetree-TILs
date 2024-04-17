n = int(input())
val = 0
for i in range (1, n):
    if n % i == 0:
        val += i
if n == val:
    print("P")
else:
    print("N")