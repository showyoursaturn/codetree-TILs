s = int(input())
age = int(input())

if s == 0:
    print('MAN') if age >= 19 else print('BOY')
if s == 1:
    print('WOMAN') if age >= 19 else print('GIRL')