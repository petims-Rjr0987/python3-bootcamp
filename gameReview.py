import random

while True:
    number_secret =random.randint(1 , 10)
    print("guess the number")
    attempts = 5
    while True:
          try:
            myChoice = int(input("Guess the number (1-10): "))
            if myChoice == number_secret:
               print("Bravo ! Tu as trouvé.")
               break
            elif myChoice< number_secret:
                print("to low !")
            else :
                print("to high")
            attempts -=1
            if attempts == 0:
                print(f"you're lose the game right anwer is {number_secret}")
                break
            
          except ValueError:
            print("it not whole number try again")
    while True:
            lastChoice = input("Do you want to play again? :")
            if(lastChoice == "oui"):
                break
            elif lastChoice == "no":
                print("BeyBey see you newt time")
                exit()
            else:
                print("invalid answer try again")
for i in range(1 ,2):
    print(f"hello {i}")
while True:
    for i in range(1, 3):
        print(i)
    break
#<head>