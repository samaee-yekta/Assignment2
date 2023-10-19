Name = input('Enter your name: ')
Family = input('Enter your family: ')
a = int(input('Enter first score: '))
b = int(input('Enter secound score: '))
c = int(input('Enter third score: '))

gpa = (a + b + c)/3

if gpa >=17:
    print('Great')
if gpa <17 and gpa >=12:
    print('Normal')
if gpa <12:
    print('Fail')