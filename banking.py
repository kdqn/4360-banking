username = "hi"
password = "yourmom"
print("Welcome to SE Bank, have funn :P")
print("Enter username:")
loginu = input()
print("Enter password:")
loginp = input()

if loginu == username:
    if loginp == password:
        print("Yep, you're in!")
    else:
        print("Nope, wrong pswd.")
else:
    print("nope, wrong username")
