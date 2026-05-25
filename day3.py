import random

def compare_guess(secret, choice):
    """Compare le nombre secret avec le choix du joueur."""
    if secret == choice:
        return "you win"
    elif choice > secret:
        return "too_high"
    else:
        return "too_low"
        
def app_game_play(player_name):
    """Lance le mini-jeu de devinette."""
    status = "Game program"
    print(f"\n**** Welcome to the game program, {player_name}! ***")
    print("Rules: Guess a number between 0 and 10. You have 5 attempts.")
    
    while True:
        won = False
        attempts = 5
        secret = random.randint(0, 10)
        
        while attempts > 0 and not won:
            try:
                choice = int(input("Choose a number: "))
                resultat = compare_guess(secret, choice)

                if resultat == "you win":
                    print("Well done, you win! 🎉")
                    won = True
                elif resultat == "too_high":
                    print("Too high! 📈")
                else:
                    print("Too low! 📉")
                
                attempts -= 1

                if not won and attempts > 0:
                    print(f"Remaining attempts: {attempts}")
            except ValueError:
                print("⚠️ It's not a whole number. Try again.")
                
        if not won:
            print(f"😢 Your attempts are over. The correct number was: {secret}")
            
        if not ask_yes_or_not(status):
            return

def ask_name():
    return input("Your name: ").strip()

def ask_origin():
    return input("Your origin: ").strip()

def required_name_origin(name, origin):
    """Valide que le nom et l'origine font au moins 4 caractères."""
    if len(name) < 4 or len(origin) < 4:
        print("⚠️ Name or origin too short (minimum 4 characters).")
        return False
    return True

def ask_age():
    while True:
        try:
            return int(input("Your age: "))
        except ValueError:
            print("⚠️ It's not a whole number. Try again.")

def age_status(age): 
    if age < 18:
        return "You are still a student, focus on your studies!"
    elif age < 30:
        return "Welcome to the power of youth!"
    else:
        return "You are a responsible adult."
    
def profile(name, origin, age):
    status = age_status(age)
    print(f"\nHello {name}, you are {age} years old, from {origin}. [{status}]")

def ask_yes_or_not(status_program):
    """Demande à l'utilisateur s'il souhaite recommencer."""
    while True:
        print(f"\n***** You are in the {status_program} *****") 
        answer = input("Do you want to do it again?\n1) Oui \n2) Non\nAnswer: ").strip()
        if answer == "1":
            return True
        elif answer == "2":
            print("Goodbye! 👋")
            return False
        else:
            print("⚠️ Invalid answer. Try again.")

def calculator_engine(a, b, op):
    """Effectue l'opération mathématique demandée."""
    if op == "+": return f"{a + b}"
    elif op == "-": return f"{a - b}"
    elif op == "*": return f"{a * b}"
    elif op == "/":
        if b == 0:
            return "Error: Division by zero is impossible."
        return f"{a / b}"
    return None

def run_calculator(player_name):
    """Gère l'interface utilisateur de la calculatrice."""
    while True:
        print(f"\nHello {player_name}, Welcome to the calculator program!")
        status = "Calculator program"
        calcule_termine = False
        
        while not calcule_termine:
            try:
                a = int(input("Your first number: "))
                while True:
                    op = input("Operator (+, -, *, /): ").strip()
                    if op in ["+", "-", "*", "/"]:
                        break
                    print("⚠️ Invalid operator. Try again.")
                
                while True:
                    try:
                        b = int(input("Your second number: "))
                        break
                    except ValueError:
                        print("⚠️ It's not a whole number. Try again.")

                resultat = calculator_engine(a, b, op)
                print(f"📊 Result: {resultat}")
                calcule_termine = True
            except ValueError:
                print("⚠️ It's not a whole number. Try again.")
                
        if not ask_yes_or_not(status):
            return

def filter_even_odd(start, end, even, odd):
    """Sépare les nombres pairs et impairs dans les listes correspondantes."""
    for i in range(start, end + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

def run_short_number(player_name):
    """Gère le programme de tri de nombres pairs/impairs."""
    status = "Short_number program"
    print("\n===========================================")
    print(f"*** Hello {player_name}, Welcome to the short number program ***")
    print("===========================================")
    
    while True:
        try:
            start_input = int(input("Enter your first interval: "))
            end_input = int(input("Enter your end interval: "))
            
            # Tri automatique pour s'assurer que start est plus petit que end
            start, end = sorted([start_input, end_input])
            
            even = []
            odd = []
            filter_even_odd(start, end, even, odd)
            
            print(f"\nInterval [{start} - {end}]")
            print(f"Odd numbers  : {', '.join(map(str, odd)) if odd else 'None'}")
            print(f"Even numbers : {', '.join(map(str, even)) if even else 'None'}")
            
            if not ask_yes_or_not(status):
                return
        except ValueError:
            print("⚠️ It's not a whole number. Try again.")

def main():
    print("=== STARTING MAIN APPLICATION ===")
    while True:
        while True:
            name = ask_name()
            origin = ask_origin()
            if required_name_origin(name, origin):
                break
        
        age = ask_age() 
        profile(name, origin, age)
        
        while True:
            print("\n--- Main Menu ---")
            print("1 : Calculator")
            print("2 : Short Number (Even/Odd)")
            print("3 : Game (Guess a number)")
            print("4 : Quit")
            answer = input("Which program do you want?: ").strip()
            
            if answer == "1":
                run_calculator(name)
            elif answer == "2":
                run_short_number(name)
            elif answer == "3":
                app_game_play(name)
            elif answer == "4":
                print("Goodbye! End of application.")
                return
            else:
                print("⚠️ Invalid answer. Try again.")

if __name__ == "__main__":
    main()