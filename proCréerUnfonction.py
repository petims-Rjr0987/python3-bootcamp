import random
def créer_profile():
    while True:
        nameUser = input("your name? :")
        country = input("country ?: ")
        if len(nameUser) < 4 and len(country )<4:
            print("name and country least 4 character try again")
        else :
            break
    while True:
            try :
                age = int(input("your age ?:"))
                if age < 18:
                    status ="You need to study more"
                elif age>= 18 or age> 30:
                    status ="Welcom to the strenght of the age"
                else:
                    status ="you should can save the others in big problème not simple problème"
                break
            except ValueError:
                print("its not whole number try again")
    print(f"Hello {nameUser} you are {age} years old next years you will be {age +1}")
    print(f"{status}")
    return nameUser
def trier_number(): 
        """Demande un intervalle et sépare pairs et impairs"""
        print("--- Analyseur de nombres ---")
        while True:
            try:
                first = int(input("First interval :"))
                end = int(input("end of interval"))
                pairs =[]
                impairs =[]
                for num in range(first , end +1):
                    if num %2 ==0:
                        pairs.append(num)
                    else:
                        impairs.append(num)
                print(f"pair : {pairs}")
                print(f"impair : {impairs}")
                break
            except ValueError:
                print("it not whole numbre try again")

def calculatrice() :
    """Programm calculatrice"""
    print("Welcom to the calculatrice programm")
    while True:
        try:
            a = float(input("First number :"))
            op = input("Operateur (+,/,*,-):")
            b = float(input("Second number :"))
            if(op == "+"): print(f"resultat : {a + b}")
            elif(op == "-"): print(f"resultat : {a - b}")
            elif(op == "/"): print(f"resultat : {a / b}")
            elif(op == "*"): print(f"resultat : {a * b}")
            
            else:
                print("Opération invalide.")
            answer = input("Do you want try again yes/no :")
            if answer == "no" and answer != "yes":
                break
        
        except ValueError:
            print("erreur de saisir")


def game() :
    while True:
        print("****welcom to the guess game******")
        secret_numbre = random.randint(1, 10)    
        while True:
            try:
                myNumber = int(input("Guess one number between (1-10) :"))
                if myNumber == secret_numbre:
                    print("Imazing, You are win 🔥")
                    break
                elif myNumber< secret_numbre:
                    print("to low")
                else:
                    print("to high")
                #<head>
                
            except ValueError:
                print("it not whole number try again")
        while True:
            aswerForAgain = input("Do you want to play again? yes/no: ").lower().strip()
            if aswerForAgain == "yes":
                break
            elif aswerForAgain == "no":
                print("Beybey see you next time")
                exit()
            else:
                print("invalid answer try egain")

def main() :
    nom = créer_profile()
    while True:
        choice = input(f"Hello {nom} What are you interested in (1 :calculatrice ,2 :myProfil,3: trier_number ,4: Quiter ,5 :game  :)")
        if choice == "1":
            calculatrice()
        elif choice == "2":
            créer_profile()
        elif choice == "3":
            trier_number()
        elif choice == "5":
            game()
        elif choice == "4":
            print("BeyBey")
            return
        else:
            print("Choice invalid")

main()