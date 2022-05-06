import random

print("The Number Is Between 1 and 10 ")

num = random.randint(1,10)



chances = 0

while chances <5:
    guess = input("Enter Your Guess : ")

 


if guess == num:
    print("Congratulations YOU WON!!!!","The Number Was",num)
   
else:
    print("The Number You Guessed is Wrong")
    chances = chances+1
if not chances <5:
    print("You Lost The Number is : ",num)




    
