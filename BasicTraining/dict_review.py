tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)
for key,value in spread.items():
  print("Your " + key +" is the "+ value+" card." )
  
  

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key,value in zip(letters,points)}
#print(letter_to_points)
letter_to_points.update({" ":0})
#print(letter_to_points)

def score_word(word):
    word = word.upper()
    point_total = 0
    for letter in word:
        if letter_to_points[letter] !=0:
            point_total += letter_to_points[letter]
    return point_total
  
#print(score_word("dwayne"))
score_word("dwayne")


player_to_words = {"player":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}

players_to_points = {}
player_points= 0      
def play_word(player, lis):
    newlist = lis
    player_to_words.update({player:newlist})
    
def update_leaderboard(play,lis):
    play_word(play,lis)
    player_points= 0 
    for key,value in player_to_words.items():
        for i in value:
            #print(i)
            player_points+= score_word(i)
        print(key + " = "+ str(player_points))
        player_points = 0
    
update_leaderboard("Dwayne",["read","rumble","sleep"])
