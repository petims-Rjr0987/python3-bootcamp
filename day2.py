import random
for i in range(5 , 1, -1):
      print(f"{i}")
""" !!!forbidden loop nolimit
while True:
       print(f"{i}")"""
while True:
            reponse = input("Do you want enter do te dark programe? (YES/NO) : ").lower()
            if reponse == "yes":
                    while True:
                        reponse1 =  input("Do you want to enter in calculatrice programmation or game?(yes/no/game) : ").lower()
                        if reponse1=="yes":
                             while True:
                                try:
                                     nmbr = int(input("enter your number to multiplication :"))
                                     for i in range(1, 51):
                                            print(f"{i}*{nmbr} : {i*nmbr}")
                                     break

                                except ValueError:
                                     print("enter valid number :")
                        elif reponse1=="game":
                              number = random.randint(1, 10)
                              while True:
                                    try:
                                        geuss = int(input("Geuss the number tetwen (1-10):"))
                                        if geuss>10:
                                          print("to hignt")
                                        elif geuss<1:
                                          
                                          print("to low")
                                        
                                        else:
                                          print("🎉 Correct! You win!")
                                          print(f"You found it in {attempts} attempts!")
                                          break
                                    except ValueError:
                                         print("don't use symbol or chaine")
                        elif reponse1=="no":
                             print("Bey")
                             break
                        else:
                             print("error :don't use symbol or number, try egain")
              
                    break
            elif reponse=="no":
                    print("Goodbey")
                    break
            else:
                     print("Erreur!!!: Don't use number or symbol try again")



   