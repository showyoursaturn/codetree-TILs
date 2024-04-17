n = int(input())
val = 0

for i in range(n):
    a = int(input())
    val += a

print(val, round(val/n, 1))