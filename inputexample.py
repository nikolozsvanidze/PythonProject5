name=input("What is your name? ")
print("hello", name)
age = input("How old are you? ")
try:
    age= int(age) # I am trying to convert it to number
    print("you were probably born in ", 2024 - age)
except ValueError:
    print("you are trying to trick me")
    print("better luck next time ")
except:
    print("something unexpected happaned")
else: #this happanes if no errors occurred
    print("you were probably born in" , 2024 - age)
finally:
    print("thanks for playing")

