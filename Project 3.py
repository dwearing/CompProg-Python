########
#import modules
#######

########
#define functions
#######
#   ESCAPE THE WOODLAND MANSION
#   You're in a woodland mansion, starting in the dining room. You can go into the hallway or kitchen. From the hallway, you can go to the foyer where the front door is. From here, you can go upstairs where there is a master bedroom with a balcony you can jump off. 
#   the scenario:
#   you and a bunch of old friends were invited to a dinner party at a friend named Tom's mansion. Lightning strikes and the light go off, and when they snap back on a few seconds later, there is a knife in Tom's chest.
#   You have to escape the mansion with the knife without getting fingerprints on it (so you can give it to the police)
#   SPOILER: get saran wrap before grabbing the knife; the only way to escape/win is jumping off the balcony (with the parachute)
#   global variables: knife, saran wrap, parachute. You need to get saran wrap from the kitchen before getting the knife (so you don't get fingerprints on it). You can then get the knife from the dining room. Then, you need to get the parachute by being nosy and opening a present in the foyer to safely jump off the balcony and escape.

def start():
    print("You received a personal invitation to have dinner with an old friend from school named Tom who lives in a woodland mansion in Vermont. It's a stormy night, and when you arrive, you realize it was not just you that he invited, but a bunch of people from your old school you haven't talked to in years. It turns out he wanted to have a reunion but worried people wouldn't show up if that's what he told them it was. You all sit down at the massive dining room table and right when you're about to take a bite of your steak, lightning strikes and the lights go out.\n\nThe lights snap back on a few seconds later and Tom is sitting in his chair with a knife in his chest.\n\nYou have to take the knife to give it to the police and escape the mansion before you're next. Make sure you don't get your fingerprints on the knife.")
    diningroom()

def diningroom():
    print("You are in the dining room")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tkitchen\n\thallway\n\tgrab the knife\n")
    if move.lower() == "kitchen":
        kitchen()
    elif move.lower() == "hallway":
        hallway()
    elif move.lower() == "grab the knife":# if they have the saran wrap, they can safely grab the knife (they don't get fingerprints on it); if they don't have saran wrap, their decision to grab the knife is bad, as they would get fingerprints on it, so I make them trip and lose
        if havesaranwrap == False:
            grab1()
        elif havesaranwrap == True:
            grab2()
    else:
        print("I'm not sure where you want to go\nTry again")
        diningroom()

def grab1():#   this happens if you try to grab the knife without first getting saran wrap to avoid fingerprints
    print("You go for the knife but you trip on a breadstick amidst the chaos and get knocked unconscious.")
    input("Press enter to restart")
    start()

def grab2():#   this happens if you try to grab the knife and got the saran wrap, safely avoiding getting fingerprints on it
    print("\nYou got the knife, now escape")
    global haveknife
    haveknife = True
    move = input("Hit enter to start escaping the dining room")
    diningroomwithknife()

def kitchen():
    print("You are in the kitchen")
    print("You see an open drawer with saran wrap and some frying pans.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tdining room\n\thallway\n\tgrab some saran wrap\n")
    if move.lower() == "dining room":
        diningroom()
    elif move.lower() == "hallway":
        hallway()
    elif move.lower() == "grab some saran wrap":
        global havesaranwrap#   if they decide to get the saran wrap, the game stores it so they can pick up the knife
        havesaranwrap = True
        kitchen_saranwrap()
    else:
        print("I'm not sure where you want to go\nTry again")
        kitchen()

def kitchen_saranwrap():
    print("Well done, now you can wrap the knife's handle with saran wrap so your fingerprints don't get on it.")
    move = input("Now press enter to get back to the dining room")
    grab2()

def diningroomwithknife():# if they already got the knife they get sent here so they can't get it again
    print("You are in the dining room")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tkitchen\n\thallway\n")
    if move.lower() == "kitchen":
        kitchen()
    elif move.lower() == "hallway":
        hallway()
    else:
        print("I'm not sure where you want to go\nTry again")
        diningroom()

def hallway():
    print("You are in the hallway")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tdining room\n\tkitchen\n\tfoyer\n")
    if move.lower() == "kitchen":#  if they already got the knife, I send them to a version of the dining room where they can't get the knife again; if they didn't already get it, they go to the dining room they started in with the knife available.
        kitchen()
    elif move.lower() == "dining room":
        if haveknife == True:
            diningroomwithknife()
        elif haveknife == False:
            diningroom()
    elif move.lower() == "foyer":
        if haveparachute == True:
            foyerwithparachute()
        elif haveparachute == False:
            foyer1()
    else:
        print("I'm not sure where you want to go\nTry again")
        hallway()

def foyer1():
    print("\nYou're in the foyer, and the front door is right in front of you.\nYou also see a wrapped christmas present laying on the floor and wonder if you should open it.")
    move = input("Where would you like to go? Say one of these choices:\n\thallway\n\tout the front door\n\tupstairs\n\topen the present\n")
    if move.lower() == "hallway":
        hallway()
    elif move.lower() == "out the front door":
        frontdoor()
    elif move.lower() == "upstairs":
        upstairs()
    elif move.lower() == "open the present":
        openpresent()
    else:
        print("I'm not sure where you want to go\nTry again")
        foyer1()

def openpresent():
    global haveparachute#   make it so the game knows they have the parachute for when they jump off the balcony
    haveparachute = True
    move = input("\nYou find a parachute in the box and save it for later\nPress enter to continue your escape")
    foyerwithparachute()

def foyerwithparachute():
    print("\nYou're in the foyer, and the front door is right in front of you.")
    move = input("Where would you like to go? Say one of these choices:\n\thallway\n\tout the front door\n\tupstairs\n")
    if move.lower() == "hallway":
        hallway()
    elif move.lower() == "out the front door":
        frontdoor()
    elif move.lower() == "upstairs":
        upstairs()
    else:
        print("I'm not sure where you want to go\nTry again")
        foyerwithparachute()

def frontdoor():
    move = input("\nThe door won't budge; the lightning knocked a tree over and it's now blocking the door\nWhere would you like to go from here? Say one of these choices:\n\thallway\n\tupstairs\n\topen the present\n")
    if move.lower() == "hallway":
        hallway()
    elif move.lower() == "upstairs":
        upstairs()
    elif move.lower() == "open the present":
        openpresent()
    else:
        print("I'm not sure where you want to go\nTry again")
        frontdoor()

def upstairs():
    print("You walk up the spiral staircase; at the top is a lone long hallway leading to the master bedroom")
    move = input("Where would you like to go? Say one of these choices:\n\tback downstairs\n\tinto the master bedroom\n")
    if move.lower() == "back downstairs":# if they already opened the present I send them to a screen where they are in the foyer but no longer care about the present; if they didn't, they will have the option to open the present
        if haveparachute == True:
            foyerwithparachute()
        elif haveparachute == False:
            foyer1()
    elif move.lower() == "into the master bedroom":
        masterbedroom()
    else:
        print("I'm not sure where you want to go\nTry again")
        upstairs()

#   you can go back downstairs, or jump off the balcony
#   jumping off the balcony is how you win, so you need the knife and parachute to do it
#   if you don't have one of these two items, you will fail and die

def masterbedroom():
    print("After questioning your life choices that have led up to this moment, you realize you have to think quickly to get out of here. You can either jump off the balcony if you think it's safe or try your luck downstairs again.")
    move = input("Where would you like to go? Say one of these choices:\n\tback downstairs\n\tjump off the balcony\n")
    if move.lower() == "back downstairs":
        if haveparachute == True:
            foyerwithparachute()
        elif haveparachute == False:
            foyer1()
    if move.lower() == "jump off the balcony":# if you jump off the balcony with the parachute and knife, you win; if you don't have one or both of these items, you lose
        if haveparachute == True and haveknife == True:
            goodending()
        elif haveparachute == False or haveknife == False:
            badending()
    else:
        print("I'm not sure where you want to go\nTry again")
        masterbedroom()


#   these are the screens you see in two of the three possible endings:

def goodending():
    print("\nCongratulations! You use your parachute to safely fly down to safety. You give the knife to the police and they identify the killer, who happened to be a national security threat. You are celebrated around the country and can relax.")

def badending():
    print("You jumped off the balcony and it was higher than you thought.")
    move = input("Press enter to restart")
    start()

########
#main
#######

#   to track whether the player actually got the knife, which you need to win
haveknife = False

#   you need saran wrap to grab the knife, so this checks whether the player has gotten it when they go for the knife
havesaranwrap = False

#   you need the parachute to jump off the balcony safely; this checks whether the player got it
haveparachute = False

start()