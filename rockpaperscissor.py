from random import randrange
print('Lets Play Rock Paper Scissor')
print('The number for rock is 1')
print('The number for paper is 2')
print('The number for scissor is 3')
a=int(input("\n Enter your number: "))
b=randrange(1,3)

# Code to display the selection
if a==1:
    print("You chose rock")
elif a==2:
    print("You chose paper")
else:
    print("You chose scissor")

if b==1:
    print("Computer chose rock")
elif b==2:
    print('Computer chose paper')
else:
    print('Computer chose scissor')


# Code to display the result
if ((a==2 and b==1) or (a==1 and b==3) or (a==3 and b==2)):
    print("You Won!!")
elif ((a==1 and b==2) or (a==3 and b==1) or (a==2 and b==3)):
    print("You Lost!!")
else:
    print("Its A Tie")

