from random import randrange
print('\n Now start guessing the number, its between 0 and 20')
a=randrange(0,20)
b=int(input('\n Enter the number:'))
while True:
    if b==a:
        break
    elif b<a:
        print("Your guess is too low")
        b=int(input('\n Enter the number:'))
    elif b>a:
        print("Your guess is too high")
        b=int(input('\n Enter the number:'))
if b==a:
    print("Great you guessed it right")
