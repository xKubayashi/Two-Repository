from time import sleep
from random import randint

print("Mini Game ^^")
sleep(2)

class Person():
    def Who_is_he(name):
        name = input("Guess the name, of the Polish thief: ")
        sleep(2)
        if name == 'Tusk' or 'tusk':
            print("Yes, it's Tusk!")
        else:
            print("You were close!")
            sleep(2)
            print("Try again.")
            sleep(2)
    
    def Guess_the_number(number):
        number = input("Guess the number, 1 - 10: ")
        sleep(2)

        los = randint(1,10)
        odp = -1
        
        while odp != los:
            i += 1
            odp = int(input("Podaj liczbę: "))
            if odp > los:
                print("The given number is less than yours")
            elif odp < los:
                print("The given number is greater than yours")
            else:
                print("None")
        print("Cool")

    
class People():
    def people(self):
        pass #Comming Soon!

result = Person()
result.Who_is_he()
result.Guess_the_number()

