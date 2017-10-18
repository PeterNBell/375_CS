def main():
    print("Welcome to ROOM BREAKER!! You have been placed in one of 16 rooms in a 4 by 4 square. There is a monster on the loose")
    print(" and a key to get out.")
    print("You will know how far away the monster is by the variable fear. Fear is how many rooms away the monster is")
    print("In each room you have 3 options: Search for the key, listen for the monster and exit the room")
    what = input("Are you ready?")
    print("GREAT!!!")
spawnroom = 0
enemyspawn = 0
from random import randrange, uniform
spawnroom = randrange(1, 16) #16 rooms, player spawns in 1
print("you are starting in room", spawnroom)
enemyspawn = randrange(1,16)
while enemyspawn == spawnroom: #if the rooms are the same the first time then make sure the rooms are different
    enemyspawn = randrange(1,16)
print("The enemy spawned in room", enemyspawn)
main()

