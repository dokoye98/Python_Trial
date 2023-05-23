

class Family:
    
    def __init__(self,input_name,input_gender,input_age = 0,input_has_children = True ):
    
        self.name = input_name
        self.gender = input_gender
        self.age = input_age
        self.childfree = input_has_children
        
    
    def new_kids(self):
        self.childfree = False
        if self.age > 28:
            print("Congratulations {name} on the child I am glad that you're {age} years old".format(name = self.name,age = self.age))
        else:
            print("what are you going to do, {name}".format(name = self.name))
    
    def __repr__(self):
        description = "Their name is {name} they are {age} years old they are {gender}".format(name = self.name, age = str(self.age),gender =self.gender)
        if self.childfree == False:
            description +=   " with children." 
        else:
            description += "  with no children."
        return description
        
fam_1 = Family("Dwayne","Male",24)
fam_2 = Family("Cassey", "Female",18)
fam_3 = Family("Mum","Female",52,False)

print(fam_1)
print()
Family.new_kids(fam_1)
print()
print(fam_1)

class Friends:
    def __init__(self, input_name,input_age = 0,input_groupsize = 0):
        
        self.name = input_name
        self.age = input_age
        self.groupsize = input_groupsize
        self.friends = []
        
    def valid_check(self,new_Friend):
        if self.groupsize <=5 and new_Friend.groupsize <2:
            self.friends.append(new_Friend)
            self.groupsize +=1
            new_Friend.groupsize +=1
            new_Friend.friends.append(self)
            print("{name1} and {name2} have become friends".format(name1 = self.name,name2 = new_Friend.name))
        else:
            print("sorry {name} you're not valid".format(new_Friend.name))
    
    
        
    
            
            
f1 = Friends("Dwayne",24,2)
f2 =Friends("nell",26,1)
Friends.valid_check(f1,f2)
        
        
