import random
def Profile_Pro():
 
    while True:
         name =  input("your name :")
         origin = input("Were do you come from? :")
         if len(name)< 4 or len(origin)<4:
             print("Age and name must least 7 character")
         else:
            break
    while True:
        try :
             age = int(input("your age ? :"))
             if age <18 :
                 status = "you are still baby focus in you study"
             elif age <40:
                 status = "Welcom to the strenght of age"
             else:
                 status = "Your are an audult"
             print(f"Hello {name} you are {age} { status} years old next years you will {age + 1} it looks like that you come from {origin}")
             while True:
                 answer = input("Do you want to try egain ?\n 1 :yes \n 2 : no :")
                 if answer != "1" and answer != "2":
                  print("invalid answer try egain")
                 elif answer == "2":
                  print("BeyBey see you next time")
                  return
                 else:
                  print("Here we go egain")
                  break
        except ValueError:
            print("Age invalid try again")

def sort_number() :
    name =""
    print(f"***Hello {name} welcom to the sort number***")
    print("we will ask for an interval and show the even number and the odd number  and the total ")
    while True:
        try:
            first = int(input("your first interval ? :"))
            end = int(input("yourlast interval :"))
            even = []
            odd = []
            count = 0
            countEven = 0
            for number in range(first , end +1):
                if number%2 == 0:
                    even.append(number)
                    countEven = countEven+1
                else:
                    odd.append(number)
                    count = count +1
            print(f"\nOur interval [{first}-{end}]")
            print(f"Pair : {even}")
            print(f"Inpair :  {odd}")
            print(f"Total even numbers : {countEven}")
            print(f"Total odd numbers : {count}")
            while True:
                UserAnswer = input("Do you want try egain? :\n 1:yes \n 2:no")
                if UserAnswer == "1":
                    break
                if UserAnswer !="1" and UserAnswer!="2":
                    print("ivalid answer try egain")
                else:
                    return




        except ValueError:
            print("int not whole number try egain ")
def game():
    print("***Welcom to the game's program***")
    
    while True:
        attemps = 6
        print("Game's rules :You Gess one number if true you win if otherwise you lose(try again or quit)")
        secret_Number = random.randint(1 ,10)
        while True:
            try:
                user_Choice = int(input("Gess one number between[1 - 10]:"))
                
                if secret_Number == user_Choice:
                    print("Well donne! you  win!")
                    break
                elif user_Choice<secret_Number:
                    print("Too low")
                else:
                    print("Too high")
                attemps -=1
                print(f"Remmainning attemps {attemps}")
                if attemps == 0:
                    print("You lost the game try again")
                    print(f"The secret number was {secret_Number}")
                    break
            except ValueError:
                    print("It's not a whole number try again")
   
        while True:
               if  Ask_Yes_or_no():
                   break
               else:
                   return
                
def calculator():
    print("****Welcom to the calculator progam****")
    while True:
            
            while True:
                try:
                    numberA = int(input("Your first number: "))
                    op = input("Operatot (*,/,-,+)")
                    numberB = int(input("your second number :"))
                    if op == "+":
                        print(f"Resultat :{numberA+numberB}")
                    elif op == "-":
                        print(f"Resultat :{numberA-numberB}")
                    elif op == "*":
                        print(f"Resultat : {numberA*numberB}")
                    elif op == "/":
                        while True:
                            if numberB == 0:
                                print("Dividing this number by zero is impossible.")
                                break
                            else:
                                print(f"resultat : {numberA/numberB} ")
                                break
                    
                    else:
                        print("Ivalid operator try again")
                    break
                except ValueError:
                    print("It's not a whole number try again:")
            while True:
                if Ask_Yes_or_no():
                    break
                else:
                    return
                
                
def main() :
     
     while True:
         print("\n===MENU===")
         print("1 :Caculator")
         print("2 :Quit")
         print("3 :sort_number")
         print("4 :game")
         print("5 :myProfile")
         answer = input("Which program ?:")
         if answer == "2":
             print("BEYBEY!")
             break
         elif answer == "4":
             game()
        
         elif answer == "3":
             sort_number()
         elif answer == "5":
             Profile_Pro()
         elif answer == "1":
             calculator()
         else :
             print("Invalid choice try egain")
        
     
def Ask_Yes_or_no():
    while True:
        answer = input("Do you want to do it again? \n1 :yes\n 2 :no \nanswer:")

        if answer == "1":
            return True
        elif answer == "2":
            print("bey bey!")
            return False
        else:
            print("Invalid answer! try again")


main()