name = "fetra"
age = 39
print("hello",name)

while True:
    name1 = input("enter your name :")
    if len(name1)  < 5:
        print("name must be 6 character up")
    elif len(name1) == 5:
        print("name must be 6 up")
    else:
       print("non, valider. On va contunue")
       break
country = input("enter your country :")
while True:
    try:
        age2 = int(input("enter your age :"))
        break
    except ValueError:
        print("this is not whole number try egain")

print("Hello", name1)
if age2<18:
    print(f"your are still baby, focus in your study, next year you will {age2 + 1}")
elif age2<=25:
    print(f"you have your own life, next year you will {age2 + 1}")
else:
    print(f"you are already audult, next year you will {age2 +1}")
a  = 1
b= 3 
print("Soustraction of",a,"and",b,"=", a - b)
print("multiplication of ",a,"and",b,"=",a*b)
answer = input("Are you want to enter in calculatrice programme?? (oui/nom):")
if(answer == "oui"):
    print("***welcome to the calculatrice programme****")
    while True:
        try:
            nmbr2 = int(input("enter your first number :"))
            nmbr3 = int(input("enter your sencond number :"))
            answer2 = input("what do you want do here(sum/mult/div/sub) : ")
            if(answer2 == "sum"):
                print("sum of ",nmbr2,"+",nmbr3,"=",nmbr2 + nmbr3)
            elif(answer2 == "mult"):
                print(f"multiplication of {nmbr2} * {nmbr3} = {nmbr2*nmbr3}")
            elif(answer2 == "div"):
                print(f"the division of {nmbr2} / {nmbr3} = {nmbr2/nmbr3}")
            elif(answer2 == "sub"):
                print(f"the substraction of {nmbr2} - {nmbr3} = {nmbr2 - nmbr3}")
            answer3 = input("Do another calculation? (oui/non) :")
            if answer3 != "oui":
                break
        except ValueError:
            print("this is not whole number try again")
    print("Beybey")
elif(answer == "non"):
    print("this is the real bey because you don't want enter in calculatrice programme bey bey")
else:
    print("beybey2")