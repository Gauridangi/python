print("Welcome to Treasure Island")
print("You have to find a treasure in this island")
print("You will face several decision. Choose wisely, as one wrong move can end the adventure")
move= input("You are the center of the island. Where do you want to go? Left/Right")
move=move.lower()
if(move=="left"):
    choice=input("you are the ocean. Do you want to do wait or swim")
    choice=choice.lower()
    if(choice=="wait"):
        door=input("A boot arrives and takes the player to a mysterious. There are three doors:Yellow,Blue and Red")
        door=door.lower()
        if(door=="yellow"):
            print("winning choice.You found the treasur!Congrulation")
        elif(door=="blue"):
          print("You are eaten by beast. Game over")
         
        elif(door=="red"):
         print("You are burned by fire. game over")
        else:
           print("You made a dumb choice.")
    elif(choice=="swim"):
        print("You are attacked by a trout. Game over")
    else:
        print("You made a dumb choice.")

elif(move=="right"):
    print("You fell into a hole. Game over.")
else:
    print("You made a dumb choice.")