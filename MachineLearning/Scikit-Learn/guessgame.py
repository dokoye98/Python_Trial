import random


answer = random.randint(1,10)

guess = int(input("guess please"))
flag = False
tries = 3
while tries > 0:

    if guess == answer:
        print("well done")
        print(answer)
        flag = True
        break
    else:
        tries-=1
        flag = False
        print(tries, " left")
        guess = int(input("guess please"))
      
print(answer)
if flag == False:
    print("game over")
else:
    print("Well Done")