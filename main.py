from account import account


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
            account = account.Account(username, password)
            account.create_account()
            for user in account.user_accounts:
                print("Account created with username and password " + user.username + "/" + user.password)
                print("1 Create new password\n2 View saved passwords\n3 Logout")
                while True:
                    choice = int(input())
                    if choice == 1:
                        username = input("Enter page name: ")
                        password = input("Enter password: ")
                        print("*******\npassword saved\n*******")
                        print("1 Create new password\n2 View saved passwords\n3 Logout")

        elif choice == 3:
            print("****************\nexited successfully\n****************")
            break
        else:
            print("Enter valid option NO")

