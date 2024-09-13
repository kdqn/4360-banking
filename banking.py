from functions import Auth, Actions

auth = Auth()

while True:
    #Break out of login loop if successful login
    if(auth.login()):
        break

account1 = Actions()
account2 = Actions()
account1.show_options(account2)  # Highlighted line
    
