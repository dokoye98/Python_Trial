import random
inventory = ["sword","axe","staff","magic spell"]


index = int(input("what number do you want? "))
choice =str(input("do you want to flip a coin? "))
reward1 = ["plasma sword", "revive"]
reward2 = ["berserk gift", "wukong staff"]
counter = 0

if inventory[index] == "sword" or inventory[index] == "magic spell":
    if choice == "yes":
        coin = random.randint(0,1)
        print("your reward is ", reward1[coin])
    else: 
        while choice != "yes" or choice !="no":
            print("choose again")
            choice =str(input("do you want to flip a coin? ")) 
            if choice == "yes":
                inventory= inventory+reward1
                print("youre new inventory is", inventory)
                break
            elif choice =="no":
                giveme = random.randint(0,len(inventory)-1)
                print("you annoyed me, give me this ", inventory[giveme])
                del inventory[giveme]
                print(inventory)
                break
           
            
            
