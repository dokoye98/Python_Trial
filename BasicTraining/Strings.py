#splitting
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)
a = []
b = []
def split_both_names(FirstList):
    both_names = [i.split() for i in FirstList]
    return both_names
    
Both_names = split_both_names(author_names)


def split_first_name(FirsList):
    first_names = [i.split()[0] for i in FirsList]
    return first_names

First_names = split_first_name(author_names)

def split_last_name(FirsList):
    last_names = [i.split()[1] for i in FirsList]
    return last_names

Last_names = split_first_name(author_names)

#joining
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = "\n".join(winter_trees_lines)
#print(winter_trees_full)


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
a = []
for name in love_maybe_lines:
  a.append(name.strip())
love_maybe_lines_stripped = "\n".join(a)
print(love_maybe_lines_stripped)

#formatting method
def intro(name,age,occupation,dream):
    temp_intro = "Hello my name is {name}. I am {age}, I am currenly working as an {occupation}. I hope to one day be able to work as a {dream}".format(name = name,occupation = occupation,dream = dream,age = age)
    return temp_intro

print(intro("Dwayne","24","Automation Tester","to open my own freelance agency"))

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
#print(highlighted_poems_list)

highlighted_poems_stripped =[]
for name in highlighted_poems_list:
  highlighted_poems_stripped.append(name.strip())

#print(highlighted_poems_stripped)
highlighted_poems_details = [i.split(":") for i in highlighted_poems_stripped]
#print(highlighted_poems_details)

titles = []
poets = []
dates = []
index = len(highlighted_poems_details)
for i in range(index):
    titles.append(highlighted_poems_details[i][0])
    poets.append(highlighted_poems_details[i][1])
    dates.append(highlighted_poems_details[i][2])
    
for i in range(index):
  print("The poem {TITLE} was published by {POET} in {DATE}.".format(TITLE =titles[i],POET = poets[i],DATE = dates[i]))
