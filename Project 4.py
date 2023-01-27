import random

transportation = ["movement towards public transport", "movement away from public transport"]#50/50 idk which will happen
population = ["massive increase", "steady increase", "steady increase"]#i think it's more likely that a steady increase will occur so i put it twice (66% chance)
renewableenergyuse = ["massively increases", "no increase", "moderately increases", "moderately increases"]#i think a moderate increase is most likely so i put it twice (50% chance)
trials = 0
trialss = 0
yearsleftwithoil = 100#this is a baseline that assumes we use little oil (compared to what we use now) in the coming years
listtoadd = []
count = 0
addedyrsleft = 0

while trialss <= 100:
    while trials <= 10000:
        transport = random.choice(transportation)
        pop = random.choice(population)
        reUse = random.choice(renewableenergyuse)
        #   say what happens to oil amnt with these scenarios; the numbers are the number of years subtracted from yrs left with oil
        if transport == "movement towards public transport":
            minustransport = random.randint(1,10)
        elif transport == "movement away from public transport":
            minustransport = random.randint(15,25)
        if pop == "massive increase":
            minuspop = random.randint(20,28)
        elif pop == "steady increase":
            minuspop = random.randint(4,8)
        if reUse == "massively increases":
            minusreUse = random.randint(2,6)
        elif reUse == "no increase":
            minusreUse = random.randint(20,28)
        elif reUse == "moderately increases":
            minusreUse = random.randint(7,10)

        yearsleftwithoil = 100 - minustransport - minuspop - minusreUse
        listtoadd.append(yearsleftwithoil)
        trials += 1
    
    while count < len(listtoadd):
        addedyrsleft = addedyrsleft + listtoadd[count]
        count += 1

    avgyearsleftwithoil = ((addedyrsleft)/len(listtoadd))
    trialss += 1
print(round(avgyearsleftwithoil,2))