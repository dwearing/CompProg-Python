#importing math for more complex mathematical functions
import math

#I will make it so if the user inputs a single term expression (ax^b) I can take the derivative
print("Give me an expression with one term (like this: ax^b) and I will take the derivative")

#store their coefficient and exponent
coefficient = input("What do you want the coefficient (a) of your expression to be?\n")
exponent = input("What do you want the exponent (b) of your expression to be?\n")

#use power rule to make the coefficient and exponent for the derivative (multiply the coefficient by the exponent and subtract 1 from exponent)
newdercfnt = int(coefficient)*int(exponent)
newderexpnt = int(exponent)-1

#tell them what their expression is so they can visualize it
print("Okay, your expression is:")
print(str(coefficient)+"x^"+str(exponent))

#this is the derivative:
der = str(newdercfnt)+"x^"+str(newderexpnt)



#ask if they want me to take the derivative, if yes: I take the derivative, if no: I say Okay then and ask if I can at least square their expression
douwantmetotakeder = input("Now do you want me to take the derivative? (yes or no)\n")
if douwantmetotakeder == "yes":
    print("The derivative is")
    print(der)
if douwantmetotakeder == "no":
    canisquare = input("Okay then, can I at least square your expression? (yes or no)\n")
    if canisquare == "yes":
        print("Okay here is your squared expression:")
        print(str(int(math.pow(int(coefficient),2)))+"x^"+str(int(exponent)*2))
    if canisquare == "no":
        print("Okay then")