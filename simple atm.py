from atexit import register


# list of registered Users in The App
registredUser = [
    {
        "name": "Deo John",
        "password": "john45",
        "cash": 70000,
        "pin": 6657,
        "userID": "0001"
    },
    {
        "name": "Sidney Snow",
        "password": "snow34",
        "cash": 76030,
        "pin": 3422,
        "userID": "0002"
    },
    {
        "name": "Carl Mark",
        "password": "mark89",
        "cash": 70000,
        "pin": 8976,
        "userID": "0003"
    },
    {
        "name": "Mike Sam",
        "password": "sam67",
        "cash": 45390,
        "pin": 1280,
        "userID": "0004"
    },
]

# Here I am defining a function that will allow the user to try again if he makes a mistake.


def try_again(keep_running):
    keep_running
    try_again = True
    count = 0
    while try_again:
        user_try = input(
            "**** Do You Want To Perform Another Transaction y for 'Yes'  and n for 'No'")
        if(user_try.lower() == 'y'):
            break
        elif(user_try.lower() == 'n'):
            keep_running = False
            break
        else:
            count += 1
            if count == 2:
                print("**** Thank You For Using Our ATM \n ****")
                keep_running = False
                break
            print("*** Invalid Entery. You Have One More Trial ***")


# This will allow the App to keep running as long as the keep_running is True.
keep_running = True
while keep_running:
    print("**** Welcome To ZURI ATM.\n Please Enter 1 To Open Account, \n 2 To Withdraw, \n 3 To Deposit, \n 4 To Check Balance, \n 5 To Exit. \n ****")
    selection = input("Enter Your Selection: ")
    if selection == "1":
        print("**** Welcome To ZURI ATM.\n Please Enter Your Name, \n Password, \n Pin and, \n Amount To Deposit. \n ****")
        name = input("Enter Your Name: ")
        password = input("Enter Your Password: ")
        pin = input("Enter Your Transaction Pin: ")
        cash = input("Enter Your Cash: ")
        try:
            int(cash)
            int(pin)
            cash = int(cash)
            pin = int(pin)
            new_user_id = len(registredUser) + 1
            registredUser.append({
                "name": name,
                "password": password,
                "cash": cash,
                "pin": pin,
                "userID": "000" + str(new_user_id)
            })
            print("**** Your Account Has Been Created Successfully. Your UserID is 000" +
                  str(new_user_id)+" Thank You****")
            try_again(keep_running)
        except ValueError:
            print("**** Invalid Cash/Pin. Both Must Be A Number Please Try Again ****")
            try_again(keep_running)

    elif selection == "2":
        print("**** Welcome To ZURI ATM.\n Please Enter Your userID, To Withdraw \n****")
        userID = input("Enter Your UserID: ")
        userID = str(userID)
        run = 0
        for i in registredUser:
            if i["userID"] == userID:
                checker = userID
                user_name = i["name"]
                print("**** Welcome To ZURI ATM. "+user_name+" ****")
                try:
                    withdraw = int(input("Enter Amount To Withdraw: "))
                    if withdraw <= i["cash"]:
                        try:
                            pin = int(input(
                                "Enter Your Pin To Validate Withdraw: "))
                            if pin == i["pin"]:
                                i["cash"] -= withdraw
                                print(
                                    "**** Withdraw Successful. Thank You For Using ZURI ATM ****")
                                run = 1
                                try_again(keep_running)
                            else:
                                print("**** Invalid Pin ****")
                                run = 1
                                try_again(keep_running)

                        except:
                            print("**** Invalid Pin. ****")
                            run = 1
                            try_again(keep_running)

                    else:
                        print("**** You Have Insufficient Funds. ****")
                        run = 1
                        try_again(keep_running)
                except:
                    print("**** Invalid Input For Amount. ****")
                    run = 1
                    try_again(keep_running)
        if(run == 0):
            print("**** Invalid UserID ****")
            try_again(keep_running)
    elif selection == "3":
        print("**** Welcome To ZURI ATM.\n Please Enter Your userID, To Deposit \n****")
        userID = input("Enter Your UserID: ")
        userID = str(userID)
        run = 0
        for i in registredUser:
            if i["userID"] == userID:
                user_name = i["name"]
                print("**** Welcome To ZURI ATM. "+user_name+" ****")
                try:
                    deposit = int(input("Enter Amount To Deposit: "))
                    i["cash"] += deposit
                    print("**** Deposit Successful. Thank You For Using ZURI ATM ****")
                    run = 1
                    try_again(keep_running)
                except:
                    print("**** Invalid Input For Amount. ****")
                    run = 1
                    try_again(keep_running)
        if(run == 0):
            print("**** Account Not Found. Please Try Again. ****")
            try_again(keep_running)
    elif selection == "4":
        print(
            "**** Welcome To ZURI ATM.\n Please Enter Your userID, To Check Balance \n****")
        userID = input("Enter Your UserID: ")
        userID = str(userID)
        run = 1
        for i in registredUser:
            if i["userID"] == userID:
                user_name = i["name"]
                print("**** Welcome To ZURI ATM. "+user_name+" ****")
                print("**** Your Current Balance is: #"+str(i["cash"])+" ****")
                run = 0
                try_again(keep_running)
        if(run == 1):
            print("**** Account Not Found. Please Try Again. ****")
            try_again(keep_running)
    elif selection == "5":
        print("**** Thank You For Using Our ATM ****")
        keep_running = False
    else:
        keep_running = False

print("*********** Thank You For Using ZURI ATM. See You Some Other Time. ***********")
