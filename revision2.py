age = int(30)
name = "Rabia"
reponse = bool("oui")
print(f"bonjour {name} tu es {age} l'année derniere tu aura {age +1}")



while True:
        nameUser = input("Your name? :")
        
        country = input("your country?:")
        if len(nameUser) <6 or len(country) < 4 :
                print("Error: Name must be at least 6 characters AND country at least 4.");
        else :
                print("name and country valid");
                break

while True:
        try:
                UserAge = int(input("your age? :"))
                if(UserAge < 18):
                        status= "your need to study more"
                elif(UserAge>= 18 and UserAge<30):
                        status = "you should have your own things"
                else:
                        status = "you are and audult "
                break
        except ValueError:
                print("It not whole nummber try again")

        #<head>      
print("*************Your full profile : ***********")
print(f"name : {nameUser} you are {UserAge} next year you will {UserAge +1}");    
print(f"{status} and its looks  like that you come from {country}")
while True :
        answer =input("Do you want to enter in the mathematics program?? yes/no :").lower().strip()
        if(answer == "yes"):
                print("Welcom to the mathematics prigamm")
                break
        elif answer == "no":
                print("BEYBEY")
                exit()
        else:
                print("Error: Enter valid answer, try again :")

