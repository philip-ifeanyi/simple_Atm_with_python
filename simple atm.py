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

# Here I am defining a function that will allow the user to try again if he makes a mistake or done with a transaction and want to try another


def try_again():
    global keep_running
    try_again = True
    # the try again gives you just two chances. So the count will keep track of how many times you have tried again
    count = 0
    while try_again:
        user_try = input(
            "**** Do You Want To Perform Another Transaction y for 'Yes'  and n for 'No'")
        # so once you select y it will allow you to run the App again
        if(user_try.lower() == 'y'):
            break
        # if you select n it will exit the App by updating keep_running to False
        elif(user_try.lower() == 'n'):
            keep_running = False
            break
        else:
            # if you select a wrong option it will ask you to try again while updating the count so that you can only try again twice
            count += 1
            if count == 2:
                print("**** Thank You For Using Our ATM \n ****")
                keep_running = False
                break
            print("*** Invalid Entery. You Have One More Trial ***")


keep_running = True
# This will allow the App to keep running as long as the keep_running is True.
while keep_running:
    # I am telling the user what the App is all about.
    print("**** Welcome To ZURI ATM.\n Please Enter 1 To Open Account, \n 2 To Withdraw, \n 3 To Deposit, \n 4 To Check Balance, \n 5 To Exit. \n ****")
    # Allowing the user to make a selection
    selection = input("Enter Your Selection: ")
    # if 1 it means you want to create a new account
    if selection == "1":
        print("**** Welcome To ZURI ATM.\n Please Enter Your Name, \n Password, \n Pin and, \n Amount To Deposit. \n ****")
        name = input("Enter Your Name: ")
        password = input("Enter Your Password: ")
        pin = input("Enter Your Transaction Pin: Please Use Just four Digits: ")
        cash = input("Enter The Amount to deposit. Must be numeric: ")
        # Here I am using a try and except to ensure that the amount and pin is numeric
        try:
            int(cash)
            int(pin)
            cash = int(cash)
            pin = int(pin)
            # here I am getting the length of the list so that I can get a new userID for the new user
            new_user_id = len(registredUser) + 1
            # I am creating a new user with the information that the user entered
            registredUser.append({
                "name": name,
                "password": password,
                "cash": cash,
                "pin": pin,
                "userID": "000" + str(new_user_id)
            })
            print("**** Your Account Has Been Created Successfully. Your UserID is 000" +
                  str(new_user_id)+" Thank You****")
            # I am calling the function try_again to allow the user to try another transaction if he or she wants
            try_again()
            # if the amount and pin you provided is not a number it will give you an error message and ask if you want to try again
        except:
            print("**** Invalid Cash/Pin. Both Must Be A Number Please Try Again ****")
            try_again()
    # if selection is 2. That is you want to withdraw
    elif selection == "2":
        # Your userID will be asked to verify your Identity
        print("**** Welcome To ZURI ATM.\n Please Enter Your userID, To Withdraw \n****")
        userID = input("Enter Your UserID: ")
        userID = str(userID)
        run = 0
        # here I am looping through the registered user list to get details of that user
        for i in registredUser:
            # if a user is found with the userID that you provided
            if i["userID"] == userID:
                user_name = i["name"]
                print("**** Welcome To ZURI ATM. "+user_name+" ****")
                # here I am using try and except to catch the amount you want to withdraw
                try:
                    withdraw = int(input("Enter Amount To Withdraw: "))
                    # if the amount is less than of equal to your available balance in the bank.
                    if withdraw <= i["cash"]:
                        try:
                            # Here I am asking for your transaction pin to validate your transaction.
                            pin = int(input(
                                "Enter Your Pin To Validate Withdraw: "))
                            # once you provide the right pin withdrawal is successful
                            if pin == i["pin"]:
                                # here I am updating the balance of the user
                                i["cash"] -= withdraw
                                print(
                                    "**** Withdraw Successful. Thank You For Using ZURI ATM ****")
                                run = 1
                                try_again()
                                # if the pin you provided is not valid it will give you an error message and ask if you want to try again
                            else:
                                print("**** Invalid Pin ****")
                                run = 1
                                try_again()
                            # if the pin you provided is not a number it will give you an error message and ask if you want to try again
                        except:
                            print("**** Invalid Pin. ****")
                            run = 1
                            try_again()
                        # if the amount you want to withdraw is greater than your available balance in the bank.
                    else:
                        print("**** You Have Insufficient Funds. ****")
                        run = 1
                        try_again()
                    # if the amount you provided is not a number it will give you an error message and ask if you want to try again
                except:
                    print("**** Invalid Input For Amount. ****")
                    run = 1
                    try_again()
        # if the userID you provided is not valid it will give you an error message and ask if you want to try again
        if(run == 0):
            print("**** Invalid UserID ****")
            try_again()
    # if selection is 3. That is you want to deposit
    elif selection == "3":
        print("**** Welcome To ZURI ATM.\n Please Enter Your userID, To Deposit \n****")
        userID = input("Enter Your UserID: ")
        # Asking for your userID
        userID = str(userID)
        run = 0
        # here I am looping through the registered user list to get details of that user
        for i in registredUser:
            # if a user is found with the userID that you provided
            if i["userID"] == userID:
                user_name = i["name"]
                print("**** Welcome To ZURI ATM. "+user_name+" ****")
                # here I am using try and except to catch the amount you want to deposit
                try:
                    deposit = int(input("Enter Amount To Deposit: "))
                    # Here I am updating the amount in the bank with the amount you deposited
                    i["cash"] += deposit
                    print("**** Deposit Successful. Thank You For Using ZURI ATM ****")
                    run = 1
                    try_again()
                    # if the amount you provided is not a number it will give you an error message and ask if you want to try again
                except:
                    print("**** Invalid Input For Amount. ****")
                    run = 1
                    try_again()
        # if the userID you provided is not valid it will give you an error message and ask if you want to try again
        if(run == 0):
            print("**** Account Not Found. Please Try Again. ****")
            try_again()
    # if selection is 4. That is you want to check your balance
    elif selection == "4":
        print(
            "**** Welcome To ZURI ATM.\n Please Enter Your userID, To Check Balance \n****")
        userID = input("Enter Your UserID: ")
        # Asking for your userID
        userID = str(userID)
        run = 0
        # here I am looping through the registered user list to get details of that user
        for i in registredUser:
            # if a user is found with the userID that you provided
            if i["userID"] == userID:
                user_name = i["name"]
                print("**** Welcome To ZURI ATM. "+user_name+" ****")
                # here I am printing the balance of the user
                print("**** Your Current Balance is: #"+str(i["cash"])+" ****")
                run = 1
                try_again()
        # if the userID you provided is not valid it will give you an error message and ask if you want to try again
        if(run == 0):
            print("**** Account Not Found. Please Try Again. ****")
            try_again()
    # if selection is 5. That is you want to exit
    elif selection == "5":
        print("**** Thank You For Using Our ATM ****")
        # I am setting keep_running to false to end the ATM CLI APP
        keep_running = False
    # if selection is not 1,2,3,4,5 it will give you an error message and ask if you want to try again
    else:
        print("**** Invalid Entery ****")
        try_again()
# End of the program
print("*********** Thank You For Using ZURI ATM. See You Some Other Time. ***********")
