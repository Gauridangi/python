print("Welcome to Haunted Mansion")
print("The mansion is full of traps")
move = input("You stand in fornt of a spooky old mansion.Do you Enter or Run away?").lower()
if(move == "enter"):
    direction = input("Choose a path inside the mansion,you see two paths. Dou you go Left or Right?").lower()
    if(direction == "left"):
        sound = input("Lead to a puzzal  room. i speak without a mouth and hear without ears.What am I?").lower()
        if(sound == "echo"):
            door = input("Correct answer. After solving the puzzle,you find three doors. They are Gold,Sliver,Black").lower()
            if(door == "gold"):
                colour = input("Winning choice. You escaped the mansion! Congratulation!")
                
            elif(door == "silver"):
                print("The door locks behind you, trapping you foreever. Game over")
            elif(door == "black"):
                print("A swarm of bats attacks you. Game over")
            else:
                print("You made a dumb choice.")
        elif(sound == "girl"):
            print("You are trapped. Game over")
        else:
            print("You made a dumb choice.")

    elif(direction == "right"):
        print("You fell through a trapdoor into the darkness and vanished. Game over")
    else:
        print("You made a dumb choice.")
elif(move == "run away"):
    print("You fled in fear.game over")
else:
    print("You made a dumb choice.")