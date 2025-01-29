from random import choice
drinks = ["gim", "vodka", "wiskey", "rum", "tequila", "absinthe" "sake"]
#print(choice(drinks))
name = input("I am a virtual bartender. What is your name? ")
try:
    age = input("What is your age? ")
    age = int(age)
    country = input("What is your country? ")
    legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "luxemburg":
        legal = True
except ValueError:
    print("Don't play games with me")
else:
    if legal:
        print("Dear", name, "It's my pleasure to serve you", choice(drinks))
    else:
        print("Dear", name, "Unfortunately I can not serve you")


