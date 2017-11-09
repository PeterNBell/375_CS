

#This is a program
import random
Player_win = False
num_players = 0
dicetotal = 0
roll_total = 0
Players = []
Scores = []
Current_player = ""

def main():
   global dicetotal
   global Turn
   global Current_player
   welcome_screen()
   playernames()
   Player_win = False
   while Player_win == False :
       scoreboard()
       for i, v in enumerate (Players):
           if Player_win == False :
            Current_player = v
            play_turn()
            current_score =Scores.pop(i)
            new_score = current_score + dicetotal
            Scores.insert(i, new_score)
            if new_score >= 100:
                endgame()
                Player_win = True





def endgame():
    global Current_player
    print("Congradulations to",Current_player ,"!!! You are the PIG god")

def scoreboard():
   global Players
   global Scores
   print("Scoreboard")
   print("----------")
   for i, v in enumerate (Scores):
       print(Players[i], v, "Points")
       print("______")




def welcome_screen():
   print("""
     ,:´'*:^-:´¯'`:·,                        ',:'/¯/`:,                    __'
    '/::::/::::::::::;¯'`*:^:-.,            /:/_/::::/';'           ,.·:'´::::::::`'·-.
   /·´'*^-·´¯'`^·,/::::::::::::'`:,         /:'     '`:/::;        '/::::::::::::::::::';
   '`,             ¯'`*^·-:;::::::'\'       ;         ';:';       /;:· '´ ¯¯  `' ·-:::/'
     '`·,                     '`·;:::i'      |         'i::i      /.'´      _         ';/' 
        '|       .,_             \:'/'       ';        ;'::i    ,:     ,:'´::;'`·.,_.·'´.,    
        'i       'i:::'`·,          i/'       'i        'i::i'   /     /':::::/;::::_::::::::;
        'i       'i::/:,:          /'          ;       'i::;' ,'     ;':::::'/·´¯     ¯'`·;:::¦
         ;      ,'.^*'´     _,.·´           ';       i:/'  'i     ';::::::'\             ';:';
         ';     ;/ '`*^*'´¯                   ';     ;/ °   ;      '`·:;:::::`'*;:'´      |/'
          \    /                               ';   / °      \          '`*^*'´         /'  
           '`^'´                                `'´       °    `·.,               ,.-·´
                                                                   '`*^~·~^*'´
   """)
   print("So you wanna play Pig Huh. I hope you do not bust!")

def dice_roll():
   global roll_total
   die1 = random.randrange(1, 7)
   roll_total = die1
   print()
   print(" +---+   ")
   print(" |", die1, "|")
   print(" +---+   ")
   print()

def play_turn():
   global dicetotal,roll_total
   global Players
   global Current_player
   print("It is", Current_player, "'s turn")
   print("")
   keepplaying = (input("Press Y to keep rolling. Do anything else to stop yourself") == 'Y')
   bust = False
   dicetotal = 0
   roll_total = 0
   while keepplaying:
       dice_roll()
       if roll_total == 1:
           dicetotal = 0
           keepplaying = False
           bust = True
           print("Tough go!", Current_player, "just busted!")
           print("")
           dicetotal = 0
           roll_total = 0
       else:
           dicetotal = dicetotal + roll_total
           print(Current_player, "has a total of", dicetotal)
           keepplaying = (input("Press Y to keep rolling. Do anything else to stop yourself") == 'Y')
   if bust == False:
        print(Current_player, "Was smart and left with", dicetotal, "points")
        print("")




def playernames():
   global Players
   global num_players
   global Current_player
   new_name = 1
   num_players = 0
   while new_name == 1:
       next_player = input("Input a player name or press enter to continue")
       if next_player != "":
           Players.insert(num_players, next_player)
           Scores.insert(num_players, 0)
           num_players = num_players + 1
       else:
           new_name = 0
       print("Here are the players: ", Players)
   print("Hi", Players, "Welcome to PIG")
main()



