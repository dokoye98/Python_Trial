class Student:
    pass

    def __init__(self,name, year):
        self.name = name
        self.year = year
        self.grades = []
    def add_grade(self,grade):
        if type(grade) is Grade:
            self.grades.append(grade)
            print("grade added")

        

roger = Student("Roger van der Weyden",10)
sandro = Student("Sandro Botticelli",12)
pieter = Student("Pieter Bruegel the Elder,",8)

class Grade:
    minimum_passing = 65
    def __init__(self,score):
        self.score = score
    def __repr__(self):
        description = "{score}".format(score = self.score)
        return description
    def is_passing(self):
        if self.score > 50:
            return "well done you pass"
        else:
            return "you fail"
        
g1 = Grade(100)
pieter.add_grade(g1)



print(type(g2))