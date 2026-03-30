username = "admin"
password = "password123"
access = False
uninput = ""
pwinput = ""
"The information in this program can only be accessed by the admin"
while access != True:
    uninput = input("username: ")
    pwinput = input("password: ")
    if (uninput != username or pwinput != password):
        print("The username or password provided is wrong, please try again")
print("Welcome admin, the secret info is")