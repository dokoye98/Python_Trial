import random
invent = ["sword","shield","axe","hammer"]
health = 100
item = ""
for a in range(10):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if health <=0:
        print("game over")
        break
    if dice1 + dice2 >=10:
        print("chest discovered")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 + dice2 >=10:
            dice1 = random.randint(1,3)
            if dice1 == 1:
              item += "gun"
              print(item)
            elif dice1 == 2:
              item += "sniper"
              print(item)
            else:
                print("sorry no item")
                
            invent += item
            print(invent)
        else:
             print("monster encountered")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)            
        if dice1 + dice2 <=10:
            health -=25
            print(health)     
    
    else:
        print("monster encountered")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)            
        if dice1 + dice2 <=10:
            health -=25
            print(health)
    
    if health <=0:
        print("game over")
        break
    
    
            
    
    
    


    
