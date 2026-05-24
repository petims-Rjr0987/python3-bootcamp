import random
def create_profile():
    while True:
        nameUser = input("your name? :")
        country = input("country ?: ")
        if len(nameUser) < 4 or len(country )<4:
            print("name and country least 4 character try again")
        else :
            break
    while True:
            try :
                age = int(input("your age ?:"))
                if age < 18:
                    status ="You need to study more"
                elif  age> 30:
                    status ="Welcom to the strenght of the age"
                else:
                    status ="you should can save the others in big problème not simple problème"
                break
            except ValueError:
                print("it's not whole number try again")
    print(f"Hello {nameUser} you are {age} years old next years you will be {age +1}")
    print(f"{status}")
    return nameUser
def sort_numbers(): 
        while True:
             """Ank for interval and distinguish the odd and the even"""
             print("--- Analyseur de nombres ---")
             while True:
                    try:
                        first = int(input("First interval :"))
                        end = int(input("end of interval:"))
                        odd_number =[]
                        even_number =[]
                        for num in range(first , end +1):
                            if num %2 ==0:
                                even_number.append(num)
                            else:
                                odd_number.append(num)
                        print(f"Even_number : {even_number}")
                        print(f"Odd_number : {odd_number}")
                        break
                    except ValueError:
                        print("it's not a whole numbre try again")
             while True:
                 if ask_yes_or_not():
                    break
                 else:
                    return 
def calculator() :
    """Programm calculatrice"""
    print("Welcom to the calculatrice programm")
    while True:
        try:
            a = float(input("First number :"))
            op = input("Operator (+,/,*,-):")
            b = float(input("Second number :"))
                
            if(op == "+"): print(f"resultat : {a + b}")
            elif(op == "-"): print(f"resultat : {a - b}")
            elif(op == "/"): 
                while True:
                    if b ==0:
                        print("Dividing this number by zero is impossible.")
                        break
                    else:
                        print(f"Resultat: {a/b}")
                        break
            elif(op == "*"): print(f"resultat : {a*b}")
            

            
            else:
                print("Invalid operator.")
            break
        
        except ValueError:
            print("input error")
    while True:
        if ask_yes_or_not():
            break
        else:
            return


def guess_game() :
    while True:
        print("****welcom to the guess game******")
        secret_numbre = random.randint(1, 10)  
        attempts = 5  
        while True:
            try:
                myNumber = int(input("Guess one number between (1-10) :"))
                if myNumber == secret_numbre:
                    print("Amazing, You win 🔥")
                    break
                elif myNumber< secret_numbre:
                    print("too low")
                else:
                    print("too high")
                attempts -=1
                if attempts == 0:
                    print(f"You  lost the game right answer is {secret_numbre}")
                    break
                #<head>
                
            except ValueError:
                print("it's not whole number try again")
        while True:
            if ask_yes_or_not():
               break
            else:
                return
def ask_yes_or_not():
    while True:
        answer = input(
        "Do you want to do it again?:\n"
        "1 : yes\n"
        "2 : no\n"
        "answer:")
        if answer == "1":
            return True
        elif answer == "2":
            print("Bye bye")
            return False
        else:
            print("Invalid answer try again")
            
def main():
    name = create_profile()

    while True:
        print("\n==== MENU ====")
        print("1. Calculator")
        print("2. Profile")
        print("3. Sort Numbers")
        print("4. Game")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            create_profile()
        elif choice == "3":
            sort_numbers()
        elif choice == "4":
            guess_game()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
main()