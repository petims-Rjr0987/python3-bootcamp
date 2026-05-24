import random
def ask_yes_or_no():
    while True:
        answer = input("Do you want to try egain??\n1: yes\n2: no\nanswer:")
        if answer == "1":
            return True
        elif answer == "2":
            print("Bey bey!")
            return False
        else:
            print("Invalid answer try egain")

def information():
        while True:
            name = input("Your name:")
            origin = input("Your origin:")

            if len(name)<4 or len(origin)<4:
                print("name and origin very short try egain")
            else:
                break

        while True:
                try:
                    age = int(input("your age? :"))
                    status =""
                    if age< 18:
                        status ="You're still beby  should learn so much"
                    elif age  <= 30:
                        status ="Welcome to the power of age"
                    else:
                        print("you are an audult welcome to your great experiance")
                    break
            #</head>
                except ValueError:
                    print("It not whole nummber try egain")
        print(f"Hello {name} you are {age} years old {status} next years you will  {age +1}")
        return name

def calculator():
     while True:
        print("***Welcom to the calculator programmm***")
        while True:
                try:
                    a = int(input("Enter your first number:"))
                    op = input("Operator :")
                    b = int(input("Your second number:"))
                    if op == "+":
                        print(f"Resultat : {a+b}")
                    elif op == "-":
                        print(f"Resultat : {a -b}")
                    elif op == "/":
                        if b == 0:
                            print("Cannot divide by zero")
                        else:
                            print(f"Resultat : {a/b}")
                    elif op == "*":
                        print(f"Resultat : {a*b}")
                    else:
                        print("Invalid Opeator try egain")
                    break
                    
               
                except ValueError:
                    print("It's not whole number try egain")
        while True:
            if ask_yes_or_no() :
                break
            else:
                return
                     
def Short_number():
    while True:
        print("***Welcom to the short number programm****")
        print("Note: We ask for interfaval and distinguish  the odd number and the even number")
        while True:
            try:
                FirstInterval = int(input("Your first interval:"))
                sencondInterval = int(input("Your second interval:"))
                if FirstInterval > sencondInterval:
                    FirstInterval,sencondInterval= sencondInterval,FirstInterval

                even_number = []
                odd_number = []
                for number in range(FirstInterval , sencondInterval+1):
                    if number%2 == 0:
                        even_number.append(number)
                    else:
                        odd_number.append(number)
                print(f"Our interval is between [{FirstInterval} - {sencondInterval}]")
                print(f"Odd number : {', '.join(map(str , odd_number)) if odd_number else 'none'}")
                print(f"Even number : {', '.join(map(str , even_number)) if even_number else 'none'}")
                break
            except ValueError:
                print("It's not whole number try egain")  
        while True:
            if ask_yes_or_no():
                break
            else:
                return
def get_extention(fileName):
    return fileName.split('.')[-1].lower()

def getExtention(fileNameFichier):
    return fileNameFichier.split('.')[0].lower()
def getSecondPoint(Filename):
    return Filename.split('.')[2].lower()
def game():
    while True:
        print(getSecondPoint("IMAGE.kkk.WOWO.pepe.meme"))
        print(getExtention("Image.png"))
        print(get_extention("Neymar.png"))
        print(get_extention("text.odd"))
        print("****Welcom to the game programm****")
        secrect_number = random.randint(1 , 10)
        attemps =4
        while True:
            try:
                User_Answer = int(input("Guess one number between 1 and 10:"))
            
                if User_Answer == secrect_number:
                    print("You win, WELL DONE")
                    break
                elif User_Answer<secrect_number:
                    print("Too low")
                else:
                    print("Too high")
                attemps = attemps -1
                print(f"Remainning attemps :{attemps}")
                if attemps == 0:
                    print(f"Your attempt is over. Correct number was {secrect_number}")
                    break
                
            except ValueError:
                print("It's not whole number try egain")
                ##</head>
        while True:
            if ask_yes_or_no():
                break
            else:
                return
        
def main():
    nameUser = information()
    print(f"Hello {nameUser} Welcom to the unbilivable programm")
    while True:
        print("1 : Calculator")
        print("2 : game") 
        print("3 :Profile ")    
        print("4 : Short_number")
        print("5 : Leave")
        answer = input("Witch programm are you interrested in?:")
        
        if answer == "1":
            calculator()
        elif answer == "2":
            game()
        elif answer == "3":
            information()
        elif answer == "4":
            Short_number()
        elif answer == "5":
            print("Bye bye!")
            break

          
main()