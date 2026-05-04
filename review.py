name = "fetra"
age ="10"
origin = "madagascar"
print(f"bonjour {name} tu es {age} on dirait que vous arrive à {origin}");


while True:
        name2 = input("votre nom? :");
        origin2 = input("origin? :");
        if len(name2) < 7 or len(origin2) < 7:
            print("Nom et origine très court il faut sup à 7 cara");
        else:
            print("Nom et origine validé bien! ");
            break
while True:
    try:
        age2 = int(input("age? :"));
        if age2 <0 or age2 >120:
             print("Veiullez entrer une âge realiste");
        else:
            break
    except ValueError: 
        print("ça n'est pas une nombre autre nombre :");
if(age <18):
     print(f"Bonjour {name2} tu es {age2}ans Tu es un jeune explorateur !");
     print(f"année prochaine tu aura {age2 +1} ");
elif(age < 40):
     print("");
