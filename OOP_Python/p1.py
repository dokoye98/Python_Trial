

class Family:
    
    def __init__(self,input_name,input_gender,input_age = 0,input_has_children = False ):
    
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
        
        
fam_1 = Family("Dwayne","Male",24)
fam_2 = Family("Cassey", "Female",18)
fam_3 = Family("Mum","Female",52,True)


Family.new_kids(fam_1)


class Friends:
    def __init__(self, input_name,input_age = 0, ):
        
        self.name = input_name
        self.age = input_age
        
        
