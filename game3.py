import random
print(random.randint(0,2))
scissor = 0
paper = 1
rock = 2
computerchoice=(random.randint(0,2))
userchoice=int(input("Enter 0 scissor , 1 paper, 2 rock"))
if (userchoice == computerchoice):
    print("It's a tie")
elif(userchoice == 0 and computerchoice == 1):
    print("scissor cut paper . You win")
elif(userchoice == 2 and computerchoice == 0):
    print("rock break scissor . You win")
elif(userchoice ==1 and computerchoice ==2):
    print("paper cover rock . You win")
else:
    print(" You loss")

