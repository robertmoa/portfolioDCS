username = "admin"
password = "password123"
access = False
uninput = ""
pwinput = ""
print("The information in this program is top secret can only be accessed by the admin")
while access != True:
    uninput = input("   username: ")
    pwinput = input("   password: ")
    if (uninput != username or pwinput != password):
        print("The username or password provided is wrong, please try again")
    else:
        access = True
print("Welcome admin, the secret to the best cookies is brown sugar")