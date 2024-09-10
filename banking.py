from functions import Auth, Actions

auth = Auth()
if auth.login():
    account1 = Actions()
    account2 = Actions()
    account1.show_options(account2)  # Highlighted line
else:
    print("Login failed. Please try again.")
