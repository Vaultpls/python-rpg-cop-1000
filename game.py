import random

#survive
#difficulty choose 1 easy, 2 - medium, 3 - hard  multipliers)

#weapons
#staff, bow, and sword

#DEBUG
DEBUG = False

#player vars
maxHealth = 100.0
currentHealth = 100.0
maxMana = 100.0 #useless so far
currentMana = 100.0


roomsComplete = 0
diff = 0 #1 - easy, 2 - medium, 3 - hard
diffRooms = 5

weapon = 0
armor = 0
name = ""

#weapon vars
staffDmg = 2 #3
bowDmg = 4 #2
swordDmg = 5 #1

#armor vars
lightArm = 0.1 #2
heavyArm = 0.3 #1

critchance = 0

#intro
def Intro():
    print("sample intro")

#setup
def Setup():
    name = input("What is your name, traveler? ")

    difficulty = input("Pick your poison(easy, medium, hard): ")
    if difficulty == "easy":
        diff = 1
    elif difficulty == "medium":
        diff = 2
    else:
        diff = 3

    classtype = input("Pick your calling(swordsman, bowman, mage): ")
    if classtype == "swordsman":
        weapon = 1
        armor = 1
        critchance = 10
    elif classtype == "bow":
        weapon = 2
        armor = 2
        critchance = 25
    else:
        weapon = 3
        armor = 2
        critchance = 20

#display stats at every start of tick
def displayStats():
    print("Your name: " + name)
    print("Current health: " + str(currentHealth))
    print("Current dungeon: " + str(roomsComplete))
    print("\n\n")

#the euseless end boss that does nothing
def uselessBoss():
    bossHealth = 100000 #useless but why not
    print("You've finally met your maker!")
    print("Current health: " + str(currentHealth))
    print("Monster health: " + str(bossHealth))
    action = input("Choose your action(a for attack, s for skip): ")
    if action == "a":
        print("The demon laughs at your attempt to hurt him.")
        print("You're dead.")

#heal based on current health and armor type
def Heal(health, armor):
    temp = 0
    if armor == 1:
        temp = random.randint(5,15)
        temp = temp * .9
    else:
        temp = random.randint(5,15)
    return temp
              
def Attack(weapon, enemyarmor, critchance):
    
    #conversion
    damage = 0
    enemyarmorstat = 0.0

    if weapon == 1:
        damage = staffDmg
    elif weapon == 2:
        damage = bowDmg
    else:
        damage = swordDmg

    if enemyarmor == 1:
        enemyarmorstat = lightArm
    else:
        enemyarmorstat = heavyArm


    damage = damage - (damage * enemyarmorstat)
    
    if DEBUG:
        print("DEBUG: ATTACK " +str(damage))
        print("DEBUG: ATTACK ENEMEYARMORVALUE " +str(enemyarmor))
        print("DEBUG: ATTACK ENEMYARMORSTAT" +str(enemyarmorstat))
        print("DEBUG: ATTACK CRITCHANCE" +str(critchance))
        
    if random.randint(1, 100) < critchance:
        damage = damage * 1.5
        print("Critical Strike!")
    return damage + random.randint(-1, 2)

def randMonster():
    #return health, armor, weapon
    return random.randint(1,55), random.randint(1, 2), random.randint(1, 3)

def Encounter(currentHealth):
    monsterHealth, monsterArmor, monsterWeapon = randMonster()
    while(monsterHealth > 0 and currentHealth > 0.0):
        print("Monster Health: " + str(monsterHealth))
        displayStats()
        action = input("Choose your action(a for attack, h for heal, s for skip): ")
        if action == "a":
            t = Attack(weapon, monsterArmor, critchance)
            monsterHealth =- t
            print("You hit " + str(t) + " damage!")
        elif action == "h":
            t = Heal(currentHealth)
            currentHealth =+ t
            print("You healed for " + str(t) + " points!")
        else:
            print("You do nothing!")
                
        if(monsterHealth <= 0 or currentHealth <= 0):
             break
            
        if random.randint(1,15) == 1:
            t = Heal(monsterHealth, monsterArmor)
            monsterHealth =+ t
            print("The monster healed for " + str(t) + " points!")
        else:
            t = Attack(monsterWeapon, armor, critchance)
            currentHealth =- t
            print("Monster strikes you for " + str(t) + " damage!")
    return currentHealth

Intro()
Setup()

while(currentHealth > 0.0 and roomsComplete <= diff * diffRooms):
    encNum = random.randint(1,100)
    if encNum < 50:
        currentHealth = Encounter(currentHealth)
    elif encNum > 25:
        print("Safe room!")
    else:
        #to modify later
        print("rand")
    print(str(currentHealth))
            
    roomsComplete =+ 1
    print("You completed a room!\n\n")
    
    
if currentHealth > 0.0:
    decision = input(name + ", you've bested me.  How about you try one more fight(y for yes, n for no): ")
    if decision == "y":
        uselessBoss()
    print("You won.")
else:
    print("You lost.")
