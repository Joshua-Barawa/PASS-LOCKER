
class Main:

    print("Welcome to password locker, Enter number to choose option")
    print("1 LOG IN\n2 SIGN UP\n3 EXIT")

    while True:
        choice = int(input())
        if choice == 1:
            print("****************\nLOGIN TO ACCOUNT\n****************")
            username = input("Enter username: ")
            password = input("Enter password: ")

        elif choice == 2:
            print("****************\nCREATE ACCOUNT\n****************")
            username = input("Enter username: ")
            password = input("Enter password: ")

        elif choice == 3:
            print("****************\nexited successfully\n****************")
            break
        else:
            print("Enter valid option NO")

