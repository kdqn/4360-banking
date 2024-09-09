from functions import Auth, Actions


def main():
    auth = Auth()
    if auth.login():
        account = Actions()
        another_account = Actions()  # Assuming another account for transfer
        Actions.show_options(account, another_account)
    else:
        print("Login failed. Please try again.")

if __name__ == "__main__":
    main()
