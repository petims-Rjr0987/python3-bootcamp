from organizer import files_organizer
from security import check_password_strength
from askYesOrNot import ask_yes_or_not
def main():

    status= "Big program main"
    while True:
        print("1: password checker")
        print("2: files program")
        answer = input("Witch program do you want?:")
        if answer == "1":
            password_user= input("Enter to verify :")
            result = check_password_strength(password_user)
            if result == "Strong":
                print("Strong: Very secure password.")
            elif result == "Medium":
                print("Medium: Increase the variety of characters.")
            else:
                print("Weak: The password is too short (minimum 8 characters)")
        elif answer == "2":
            path = input("Enter the full path to the folder to be stored:")
            files_organizer(path)
        else :
            print("Invalid choice!")
            continue
        if not ask_yes_or_not(status):
            print("End of the main program. Goodbye!")
            break
if __name__ == "__main__":
    main()