

#****MY EXERCICE IS SATARTING HERE**** 
        #exercice 1
print("My first exercise")
name1 = input("enter your name: ")
country1 = input("enter your country :")
while True:
        try:
                age1 = int(input("enter your age :"))
                break
        except ValueError:
                print("this is not a whole number try again")

if age1>=21:
        print(f"Hello {name1} it looks like you come from {country1} \nyou should have your own life next yoer you will {age1 +1}")

elif age1>=18:
        print(f"hello {name1} it looks like you come from {country1} \nyour are still young next year you will {age1 +1}")

else:
       print(f"Hello {name1} it looks like you come from {country1} \nyou are stil minor, next year you will be {age1 +1}")

reponse = input("Do you want to enter the calculation program? (oui/non) :").lower()
if reponse == "oui":
        while True:
                try:
                        number1 = int(input("enter your  first number !: "))
                        number2 = int(input("enter your  second number !: " ))
                        break
                except ValueError:
                        print("it not whole number try again")

        print(f"miltiplication of{number1} and {number2}: {number1*number2}")
        print(f"Subtraction of {number1} and {number2}: {number1-number2}")
        print(f"addition of {number1} and {number2} :{number1+number2}")
else:
        print(f"GOODBEY {name1}")
