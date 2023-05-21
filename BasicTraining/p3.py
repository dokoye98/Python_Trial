songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key,value in zip(songs,playcounts)}
print(plays)
plays["Purple Haze"] = 1

plays.update({"Respect":94})

library = {"The Best Songs":plays, "Sunday Feelings":{} }
print(library)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id =user_ids.get("teraCoder",100000)
print(tc_id)

stack_id =user_ids.get("superStackSmash",100000)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points +=available_items.pop("stamina grains",0)
print(health_points)
health_points +=available_items.pop("power stew",0)
health_points +=available_items.pop("mystic bread",0)
print(available_items)
print(health_points)
#.keys()
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)
#.value()

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0

for i in num_exercises.values():
  total_exercises += i

print(total_exercises)

#items
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key,value in pct_women_in_occupation.items():
  print("Women make up "+ str(value) + " percent of "+ key+"s.")