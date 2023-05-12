import random

counter =0
tailsc = 0
headc = 0
coin = ""
tries = 1
anon = 0
for b in range(10):
    for a in range(100):
        num =  random.randint(1,2)
        num2 =  random.randint(1,2)
        if num ==1:
            coin = "tails"
            tailsc+=1
            if num ==1 and num2 ==1:
             tailsc+=1
        else:
            coin = "heads"
            headc += 1
            if num ==2 and num2 ==2:
                headc += 1 
        if num != num2:
            anon += 1
    print(tailsc,headc , anon)
    anon = 0
    headc = 0 
    tailsc = 0
    


