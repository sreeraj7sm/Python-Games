from random import choice
print(' ---------------------------')
print('|     Welcome to the game    |')
print(' ---------------------------')
print("What is your name?")
name=input("")
print("Hello "+name+" lets start!!")
words=['chocolate','pink','house','tiger','wash','monkey','school']
word=choice(words)
guesses=''
turns=10
while turns > 0:
    failed=0
    for i in word:
        if i in guesses:
            print(i)
        else:
            print("_")
            failed +=1
    if failed==0:
        print("You won!!")
        print("The word was: "+word)
        break


    guess=input("Guess the character: ")
    guesses +=guess

    if guess not in word:
        turns-=1
        print("Wrong character")
        turnstr=str(turns)
        print("You have "+turnstr+" turns left")

        if turns==0:
            print("You loose!!!")


