import csv
loggedin="No"
account=input("Do you already have an account?")
if account=="No" or account=="no" or account=="n" or account=="N":
    while account=="No" or account=="no" or account=="n" or account=="N":
    #Create username and password
        createuser=input("Please create a username?")
        createpass=input("Please create a username?")
        file=open("userandpass.csv", "w")
        writer=file.write(file)
        writer.writerow(createuser,createpass)
        account="Yes"
elif account=="Yes" or account=="yes" or account=="y" or account=="Y":
    correct="No"
    numberoftries=3
    while correct=="No" or numberoftries>0:
        username=input("Please enter your username")
        file=open("userandpass.csv", "w")
        for x in file(0):
            if username==x:
                password=input("Please enter your password")
                if file(x,1)==password:
                    print("Access granted")
                    correct="Yes"
                    loggedin=="Yes"
                else:
                    print("Fail")
                    numberoftries=numberoftries-1
            else:
                print("Fail")
                numberoftries=numberoftries-1
else:
    print("Invalid input")

if loggedin=="Yes":
    