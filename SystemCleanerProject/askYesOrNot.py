import random
def compare_guess(secret,choice):
    if secret == choice:
        return "you win"
    elif choice > secret:
        return "too_high"
    else:
        return "too_low"
        
def appGamePlay(nameGamePlayer):
        status = "Game program"
        print("****Welcom to the game program***")
        print("Rules: Guess a number between 0 and 10. You have 5 attempts.e")
        while True:
           won= False
           attempts =5
           secret = random.randint(0, 10)
           while attempts > 0 and not won:
               try:
                    choice = int(input("Choose a number:"))
                    resultat= compare_guess(secret, choice)

                    if resultat == "you win":
                        print("Well done, you win!")
                        won = True
                    elif resultat == "too_high":
                        print("too high")
                    else:
                        print("too low")
                    attempts -= 1

                    if not won and attempts > 0:
                            print(f"Remaining attempts: {attempts}")
               except ValueError:
                   print("It's not whole number try egain")
           if not won:
                print(f"Your attempt is over. Correct number was: {secret}")
           if not ask_yes_or_not(status):
               return
    


def ask_name():
    return input("your name :")

def ask_origin():
    return input("Your origin:")
def required_name_origin(name , origin):
        if len(name) <4 or len(origin) <4:
            print("Name or origin too short(min 4 chars)")
            return False
        return True
       


def ask_age():

    while True:
        try:
            age = int(input("Your age :"))
            return age 
        except ValueError:
            print("It's not whole number try egain")

def age_status(age): 
    if age < 18:
        return "Your are still baby focus on study"
    if age < 30:
        return "Welcome to the power of age"
    else:
        return "Your are an adult"
    
def profile(name , origin ,  age):
    status = age_status(age)

    print(f"Hello  {name} you are {age} yers old, from {origin} ,{status}  ")
#<body>
def ask_yes_or_not(status_program):
    while True:
        print(f"*****you are in the {status_program}****") 
        asnwer = input("Do you want do it again?\n1) oui \n2) non\nanswer :")
        if asnwer == "1":
            return True
        elif asnwer == "2":
            print("Beybey")
            return False
        else:
            print("Invalid answer try again")

def calculatorEngine(a , b,op):
            if op == "+":
                return f"{a +b}"
            elif op == "-":
                return f"{a -b}"
            elif op == "*":
                return f"{a *b}"
            elif op == "/":
                if b == 0:
                    return "Erro : division with zero impasible"
                else:
                    return f"{a /b}"
            else:
              return None
def calculatorTire(nameC):
    while True:
        print(f"Hello {nameC} Welcom to the calculator program")
        status = "calculator progam"
        calcule_termine = False
        while not calcule_termine:
            try:
                a = int(input("Your first number:"))
                while True:
                    op = input("Operator :")
                    while True:
                        try:
                            b = int(input("Your second number:"))
                            break
                        except ValueError:
                            print("It's not whole number try egain")

                    resultat = calculatorEngine(a , b ,op)
                    if resultat is not None:
                        print(f"Resultat : {resultat}")
                        calcule_termine = True
                        break
                    else:
                        print("Ivalid operator try egain")
                        continue
            except ValueError:
                print("It's not whole number try again")
                continue
        if not ask_yes_or_not(status):
            return

def short_number_Fonction(start , end, even , odd):
    if start > end:
        start, end=end , start
    else:
        for i in range(start, end +1):
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)

def short_number(nameS):
    status = "Short_number program"
    print("===========================================")
    print(f"***Hello {nameS} Welcom to the short number program***")
    print("===========================================")
    print("Work : we ask an number and  distinguish the odd_number and eve_number")
    while True:
        try:
            startInterval = int(input("Enter your first interval:"))
            endInterval = int(input("Enter your end interval"))
            start , end = sorted([startInterval, endInterval])
            even = []
            odd = []
            short_number_Fonction(start, end,even, odd)
            print(f"Interval [{startInterval} - {endInterval}]")
            print(f"odd number : {','.join(map(str , odd)) if odd else 'none'}")
            print(f"even number : {','.join(map(str, even)) if even else 'none'}")
            if not ask_yes_or_not(status):
                    return
        except ValueError:
            print("It's not whole number try again")
def main():
    while True:
        status = "principal progam"
        while True:
            name = ask_name()
            origin = ask_origin()
            if required_name_origin(name, origin):
                break
        age  = ask_age() 
        profile(name,origin,age)
        while True:
            print("1 : Calculator")
            print("2 :Short_numbe")
            print("3 : Game")
            print("4 : Quiter")
            answer = input("Wich program are you want:")
            if answer == "1":
                calculatorTire(name)
            elif answer == "2":
                short_number(name)
            elif answer == "3":
                appGamePlay(name)
            elif answer == "4":
                print("beybey")
                return
            else:
                print("Invalid answer try egain")
        

if __name__ == "__main__":
    main()