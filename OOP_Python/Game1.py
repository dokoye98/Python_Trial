

class Digimon:
    
    def __init__(self,name,combat_power,colour,final_form,fusion,tamer):
        self.name = name
        self.colour = colour
        self.combat_power = combat_power
        self.final_form = final_form
        self.fusion = fusion
        self.tamer = tamer
        
        
    def evolve(self):
        if self.final_form == False and self.tamer == True:
            self.combat_power *=100
            self.final_form = True
            return "Well done {name} you have evolved.\nWow your combat power is {combat}".format(name = self.name,combat = self.combat_power)
        else:
            if self.fusion == False:
                self.combat_power  *=10
                self.fusion = True
                return "WOW {name} you fused \nYour power is {power}".format(name = self.name,power = self.combat_power)
            
    def enemy(self):
        if self.combat_power > 900 and self.tamer == True:
            return "this is easy"
        elif self.combat_power < 90 and self.tamer == True and self.final_form == False:
            print("Theres no way you though a small power of {} could beat me".format(self.combat_power))
            self.final_form = True
            self.evolve()
            return "We did it well done it was a hard fight and you evolved your new power is {}".format(self.combat_power)
        else:
            return "I lost"
    
    def greeting(self):
        
        return "hi my name is {}".format(self.name)        
    
    def __repr__(self):
        desc = "hello my name is {name} i am {colour} my combat power is {power}".format(name = self.name,colour = self.colour,power = self.combat_power)
        if self.final_form == True and self.fusion == True and self.tamer == True:
            desc += " I am at my final fusion form "
        
    
augomon = Digimon("Augumon",80,"Orange",False,False,True)
devimon = Digimon("devimon",80,"black",False,False,False)

print(devimon.enemy())

print(augomon.evolve())
print(augomon.enemy())       

class Tamer:
    
    def __init__(self, name,age,no_of_digimon) -> None:
        self.name = name
        self.age = age
        self.no_of_digimon = no_of_digimon
        self.digimon = []
        
    def greeting(self):
        
        return "hi my name is {}".format(self.name)  
    
    def add_digi(self,digimon):
        if len(self.digimon) <= self.no_of_digimon:
            self.digimon.append(digimon)
            print("hello {name} my name is {myname}".format(name =digimon.name,myname = self.name ))
        else:
            print("Sorry out of space")
    
    def release(self,digimon):
        if digimon in self.digimon:
            self.digimon.remove(digimon)
            print("goodbye {name} ".format(name =digimon.name))
        else:
            print("sorry we dont have them here")
dillian = Tamer("Dillian",20,1)

dillian.add_digi(augomon)
dillian.release(augomon)