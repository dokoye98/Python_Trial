destinations = ["Paris, France" ,"Shanghai, China","Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler =['Eiffel tower', 'Wall of beiging', 'star walkway hollywood', 'christ the redeemer',"sphyx"]
def get_destination_indext(des):
  destination_index = destinations.index(des)
  return destination_index
print(get_destination_indext("Los Angeles, USA"))



def get_traveler_location(traveler):
 # travelers_destination = ""
  traveler_destination_index = get_destination_indext(traveler)
  return test_traveler[traveler_destination_index]
  
print(get_traveler_location("São Paulo, Brazil"))


first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name,last_name):
  return first_name[0:3] + last_name[0:3]

newaccount =account_generator(first_name,last_name)

    
      