import random
r=random.randint(1,10)
print("Hey lets play a game\nGuess a number between 1 to 10")
guess=0
while(guess<11):
    n=int(input())
    guess+=1
    if(n==r):
        print("Greate, You guessed the number correct in ",guess," trials")
        break
    elif(n<r):
        print("Guess a bigger number")
    else:
        print("Guess a smaller number")
else:
    print("You lost all chance!!  Better luck next time.")
