n = int(input())
cnt = 65
for i in range(n):
    for j in range(0,i+1):
        print(chr(cnt), end = "")
        cnt += 1
        if chr(cnt) == 'Z':
            cnt = 65 
    print()