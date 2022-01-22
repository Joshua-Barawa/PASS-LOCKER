from account import account
from passwords import password


class Main:
    print("Welcome to password locker, Enter option number to continue")
    # print("1 LOG IN\n2 SIGN UP\n3 EXIT")

    while True:
        print("1 LOG IN\n2 SIGN UP\n3 EXIT")
        choice = int(input())
        if choice == 1:
            print("****************\nLOGIN TO ACCOUNT\n****************")
            username = input("Enter username: ")
            pass_word = input("Enter password: ")

            login = account.login(username)
            if not login:
                print("Invalid user credentials")
            else:
                print("Welcome back ", username, "Enter option number to continue")
                while True:
                    print("1 Create new password\n2 View saved passwords\n3 Delete password\n4 Logout")
                    choice = int(input())
                    if choice == 1:
                        page = input("Enter page name: ")
                        pass_word = input("Enter password: ")

                        new_password = password.Password(page, pass_word)
                        new_password.create_password()
                        print("*******\npassword saved\n*******")

                    elif choice == 2:
                        for password in new_password.user_passwords:
                            print("********* " + password.page, ":", password.password)

                    elif choice == 3:
                        choice = input("Enter page name: ")
                        for password in new_password.user_passwords:
                            if password.page == choice:
                                new_password.delete_password(choice)
                                print("Password Deleted!!")

                    elif choice == 4:
                        print("Logged out!!")
                        break

        elif choice == 2:
            print("****************\nCREATE ACCOUNT\n****************")
            username = input("Enter username: ")
            pass_word = input("Enter password: ")
            account = account.Account(username, pass_word)
            account.create_account()

            for user in account.user_accounts:
                print("Account created successfully")
                while True:
                    print("1 Create new password\n2 View saved passwords\n3 Delete password\n4 Logout")
                    choice = int(input())
                    if choice == 1:
                        page = input("Enter page name: ")
                        pass_word = input("Enter password: ")

                        new_password = password.Password(page, pass_word)
                        new_password.create_password()
                        print("*******\npassword saved\n*******")

                    elif choice == 2:
                        for password in new_password.user_passwords:
                            print("********* " + password.page, ":", password.password)

                    elif choice == 3:
                        choice = input("Enter page name: ")
                        for password in new_password.user_passwords:
                            if password.page == choice:
                                new_password.delete_password(choice)
                                print("Password Deleted!!")

                    elif choice == 4:
                        print("Logged out!!")
                        break
        elif choice == 3:
            print("****************\nexited successfully\n****************")
            break
        else:
            print("Enter valid option NO")

