
def IsAccauntGood(NCode, FName, LName, ANo, Balance):
    if(len(NCode.strip()) != 10 or not NCode.isnumeric()):
        print("\nError: National Code should be 10 digits!\n")
        return False
    if(len(FName.strip()) == 0 or len(FName.strip()) > 15):
        print("\nError: Invalid First Name (Max len 15 character)!\n")
        return False
    if(len(LName.strip()) == 0 or len(LName.strip()) > 20):
        print("\nError: Invalid Last Name (Max len 20 character)!\n")
        return False
    if(len(ANo.strip()) != 10 or not ANo.isnumeric()):
        print("\nError: Invalid Account No. (10 digits)!\n")
        return False
    if(Balance.strip() == "" or len(Balance.strip()) > 15):
        print("\nError: Invalid Balance (Max len 15 character)!\n")
        return False
    #Now check duplication of National Code and Account Number
    AccountFile = open("Accounts.txt","r")
    AllLines = AccountFile.readlines()
    NationalCodeFound = False
    AccountFound = False
    for OneLine in (AllLines):
        NationalCode = OneLine[1: 11]
        AccountNo = OneLine[46: 56]
        if(OneLine[0] == '1' and NCode == NationalCode):
            NationalCodeFound = True
        if(OneLine[0] == '1' and ANo == AccountNo):
            AccountFound = True
    AccountFile.close()
    if(NationalCodeFound):
        print("\nError: Dupplicated National Code!\n")
        return False
    if(AccountFound):
        print("\nError: Dupplicated Account No.!\n")
        return False
    return True
#----------------------------------------------------------------    
def SearchAnAccount():
    NCode = input("National Code: ")
    AccountFile = open("Accounts.txt","r")
    AllLines = AccountFile.readlines()
    Found = False
    for OneLine in (AllLines):
        NationalCode = OneLine[1: 11]        
        if(NCode == NationalCode):
            Found = True
            DisplayOneAccount(OneLine)
    if(not Found):
        print("\nNot Found!\n")
    AccountFile.close()
#----------------------------------------------------------------    
def DeleteAccount():
    NCode = input("National Code: ")
    AccountFile = open("Accounts.txt","r")
    AllLines = AccountFile.readlines()
    LineNo = 0
    Found = False
    for OneLine in (AllLines):
        NationalCode = OneLine[1: 11]        
        if(NCode == NationalCode):
            OneLine = '0' + OneLine[1:]
            AllLines[LineNo] = OneLine
            Found = True
        LineNo = LineNo + 1
    AccountFile.close()
    if(Found == True):
        AccountFile = open("Accounts.txt","w")
        AccountFile.writelines(AllLines)
        AccountFile.close()
        print("\nAccount Deleted!\n")
    else:
        print("\nNot Found!\n")
#----------------------------------------------------------------    
def DisplayOneAccount(OneLine):
    if(OneLine[0] == '0'):                                             
        print("***", end="")
    NationalCode = OneLine[1: 11].strip()
    FullName = OneLine[11: 26].strip() + " " + OneLine[26: 45].strip()
    AcountNo = OneLine[46: 56].strip()
    Balance = OneLine[56: 71].strip()
    #Now print    
    print("National Code: " + NationalCode, end="")
    print("    Full Name: " + FullName, end="")
    print("    Account Number: " + AcountNo, end="")
    print("    Balance: " + Balance + "\n")
#----------------------------------------------------------------    
def DisplayAccounts():
    AccountFile = open("Accounts.txt","r")
    AllLines = AccountFile.readlines()
    for OneLine in (AllLines):
        DisplayOneAccount(OneLine)
    AccountFile.close()    
        
#----------------------------------------------------------------    
def CreateAccount():
    NationalCode = input("National Code (10 digits): ")
    FirstName = input("First Name: ")
    LastName = input("Last Name: ")
    AccountNo = input("Account No. (10 digits): ")
    Balance = input("Balance (Rial): ")
    if (IsAccauntGood(NationalCode, FirstName, LastName, AccountNo, Balance)):
        AccountFile = open("Accounts.txt","a")
        NationalCode = NationalCode.ljust(10, ' ')
        FirstName = FirstName.ljust(15, ' ')
        LastName = LastName.ljust(20, ' ')
        AccountNo = AccountNo.ljust(10, ' ')
        Balance = Balance.rjust(15, ' ')        
        AccountFile.write("1")
        AccountFile.write(NationalCode)
        AccountFile.write(FirstName)
        AccountFile.write(LastName)
        AccountFile.write(AccountNo)
        AccountFile.write(Balance)
        AccountFile.write(FirstName.strip())
        AccountFile.write("\n")
        AccountFile.close()    
        print("\nRecord added!\n")
        
#----------------------------------------------------------------    
def MenuAccountManagement():
    SelectedItem = " "
    while (SelectedItem != "5"):
        print("1: Create Account")
        print("2: Delete Account")
        print("3: Search An Account")
        print("4: Display Accounts")
        print("5: Return")                                            
        SelectedItem = input()
        if(SelectedItem == "1"):
            CreateAccount()
        elif(SelectedItem == "2"):
            DeleteAccount()
        elif(SelectedItem == "3"):
            SearchAnAccount()
        elif(SelectedItem == "4"):
            DisplayAccounts()

#----------------------------------------------------------------    
def MenuAdmin():
    SelectedItem = " "
    while (SelectedItem != "2"):
        print("\n1: Account Management")
        print("2: Exit")                                              
        SelectedItem = input()
        if(SelectedItem == "1"):
            MenuAccountManagement()

#----------------------------------------------------------------    
def AccountInfo (NCode):
    AccountFile = open("Accounts.txt","r")
    AllLines = AccountFile.readlines()
    Found = False
    for OneLine in (AllLines):
        NationalCode = OneLine[1: 11]        
        if(NCode == NationalCode):
            Found = True
            DisplayOneAccount(OneLine)
    if(not Found):
        print("\nNot Found!\n")
    AccountFile.close()

#----------------------------------------------------------------    
def IsDepositGood(Amount, Date):
    if(Amount.strip() == "" or len(Amount.strip()) > 15):
        print("\nError: Invalid Amount (Max len 15 character)!\n")
        return False
    if(len(Date.strip()) != 8 or Date[2] != '/' or Date[5] != '/'):
        print("\nError: Invalid Date!\n")
        return False
    return True

#----------------------------------------------------------------    
def Deposit (UName, ANo):
    Amount = input("Amount (Rial): ")
    Date = input("Date (yy/mm/dd): ")
    if (IsDepositGood(Amount, Date)):
        TransferFile = open("Transfer.txt","a")
        Amount = Amount.rjust(15, ' ')
        Date = Date.ljust(8, ' ')
        TransferFile.write("1")
        TransferFile.write(Date)
        TransferFile.write(UName)    #Same as NationalCode
        TransferFile.write("0000000000")
        TransferFile.write(ANo)
        TransferFile.write(Amount)
        TransferFile.write("\n")
        TransferFile.close()    
        print("\nRecord added!\n")

#----------------------------------------------------------------    
def IsWithdrawGood(Amount, Date):
    if(Amount.strip() == "" or len(Amount.strip()) > 15):
        print("\nError: Invalid Amount (Max len 15 character)!\n")
        return False
    if(len(Date.strip()) != 8 or Date[2] != '/' or Date[5] != '/'):
        print("\nError: Invalid Date!\n")
        return False
    return True

#----------------------------------------------------------------    
def Withdraw (UName, ANo):
    Amount = input("Amount (Rial): ")
    Date = input("Date (yy/mm/dd): ")
    if (IsWithdrawGood(Amount, Date)):
        TransferFile = open("Transfer.txt","a")
        Amount = Amount.rjust(15, ' ')
        Date = Date.ljust(8, ' ')
        TransferFile.write("1")
        TransferFile.write(Date)
        TransferFile.write(UName)    #Same as NationalCode
        TransferFile.write(ANo)
        TransferFile.write("0000000000")
        TransferFile.write(Amount)
        TransferFile.write("\n")
        TransferFile.close()    
        print("\nRecord added!\n")

#----------------------------------------------------------------    
def IsTransferGood(FromAccountNO, Amount, Date, ToAccountNo):
    if(Amount.strip() == "" or len(Amount.strip()) > 15):
       print("\nError: Invalid Amount (Max len 15 character)!\n")
       return False
    if(len(Date.strip()) != 8 or Date[2] != '/' or Date[5] != '/'):
       print("\nError: Invalid Date!\n")
       return False
    #Check To Account NO.
    AccountFile = open("Accounts.txt","r")
    AllLines = AccountFile.readlines()
    Found = False
    for OneLine in (AllLines):
        ANo = OneLine[46: 56]        
        if(ANo == ToAccountNo):
            Found = True
    AccountFile.close()
    if(not Found):
        print("\nError: Invalid Destination Account No.!\n")
        return False
    #
    if(FromAccountNO == ToAccountNo):
        print("\nError: Should not Tranfer to the Same Account!\n")
        return False
    return True

#----------------------------------------------------------------    
def Transfer (UName, ANo):
    Amount = input("Amount (Rial): ")
    Date = input("Date (yy/mm/dd): ")
    ToAccount = input("To Account No. (10 digits): ")
    if (IsTransferGood(ANo, Amount, Date,ToAccount)):
        TransferFile = open("Transfer.txt","a")
        Amount = Amount.rjust(15, ' ')
        Date = Date.ljust(8, ' ')
        ToAccount = ToAccount.ljust(10, ' ')
        TransferFile.write("1")
        TransferFile.write(Date)
        TransferFile.write(UName)    #Same as NationalCode
        TransferFile.write(ANo)
        TransferFile.write(ToAccount)
        TransferFile.write(Amount)
        TransferFile.write("\n")
        TransferFile.close()    
        print("\nRecord added!\n")
    
#----------------------------------------------------------------    
def MenuTransfer():
    global globalUserName, globalPassword, globalAccountNo
    SelectedItem = " "
    while (SelectedItem != "4"):
        print("\n1: Deposit")
        print("2: Withdraw")
        print("3: Transfer to Another Account")
        print("4: Return")
        SelectedItem = input()
        if(SelectedItem == "1"):
            Deposit(globalUserName, globalAccountNo)
        elif(SelectedItem == "2"):
            Withdraw(globalUserName, globalAccountNo)
        elif(SelectedItem == "3"):
            Transfer(globalUserName, globalAccountNo)

#----------------------------------------------------------------    
def ShowUserTransactions(UName):
    Found = False
    TransactionFile = open("Transfer.txt","r")
    AllLines = TransactionFile.readlines()
    for OneLine in (AllLines):
        Date = OneLine[1: 9].strip()
        UserID = OneLine[9: 19].strip()
        FromAccountNo = OneLine[19: 29].strip()
        ToAccountNo = OneLine[29: 39].strip()
        Amount = OneLine[39: 54].strip()
        #Now print
        if(UName == UserID):
            Found = True
            if(OneLine[0] == '0'):                                             
                print("***", end="")
            print("National Code: " + UserID, end="")
            print("    Date: " + Date, end="")
            print("    From Account Number: " + FromAccountNo, end="")
            print("    To Account Number: " + ToAccountNo, end="")
            print("    Amount: " + Amount + "\n")
    TransactionFile.close()
    if(not Found):
        print("\n There Is No Transaction!\n")

#----------------------------------------------------------------    
def ChangePassword(UID):
    CurrenePassword = input("Current Password: ")
    NewPassword1 = input("New Password: ")
    NewPassword2 = input("Retry New Password: ")
    if(NewPassword1 != NewPassword2):
        print("\nNew Passwords Do Not Match!\n")
    #
    AccountFile = open("Accounts.txt","r")
    AllLines = AccountFile.readlines()
    Found = False
    LineNo = 0
    for OneLine in (AllLines):
        NationalCode = OneLine[1: 11]        
        P = OneLine[71:]
        P = P[0:len(P) - 1]   #Remove \n from the end of the OneLine
        if(NationalCode == UID):
            if(P != CurrenePassword):
                print("\nInvalid Current Password!")
                return;
            else:
                Found = True
                OneLine = OneLine[0:71] + NewPassword1 + "\n"
                AllLines[LineNo] = OneLine
        LineNo = LineNo + 1
    AccountFile.close()
    if(Found == True):
        AccountFile = open("Accounts.txt","w")
        AccountFile.writelines(AllLines)
        AccountFile.close()
        print("\nPassword Changed!\n")
    else:
        print("\nNot Found!\n")

#----------------------------------------------------------------    
def MenuUser():
    global globalUserName, globalPassword, globalAccountNo
    SelectedItem = " "
    while (SelectedItem != "5"):
        print("\n1: Account Info")
        print("2: Transfer")
        print("3: Show Transactions")
        print("4: Change Password")
        print("5: Exit")
        SelectedItem = input()  
        if(SelectedItem == "1"):
            AccountInfo(globalUserName)
        elif(SelectedItem == "2"):
            MenuTransfer()
        elif(SelectedItem == "3"):
            ShowUserTransactions(globalUserName)
        elif(SelectedItem == "4"):
            ChangePassword(globalUserName)

#----------------------------------------------------------------    
# this routin will return true if the user is valid otherwise will return false
def ValidUser(user_name, Pass):
    global globalAccountNo
    if(user_name.upper() == "ADMIN"):
        if(Pass == "ADMIN"):
            return True
        else:
            return False
    else:
        AccountFile = open("Accounts.txt","r")
        AllLines = AccountFile.readlines()
        Found = False
        for OneLine in (AllLines):
            NationalCode = OneLine[1: 11]
            P = OneLine[71:]
            P = P[0:len(P) - 1]   #Remove \n from the end of the OneLine
            if(OneLine[0] == '1' and user_name == NationalCode and Pass == P):
                Found = True
                globalAccountNo = OneLine[46: 56]        #Get the account NO in Global AccountNo variable
        AccountFile.close()        
        if(Found):
            return True
        else:
            return False

#----------------------------------------------------------------    
#This routin gets the username & password then if it is valid will go to UserMenu or AdminMenu
def Login():
    global globalUserName, globalPassword, globalAccountNo
    CreateDataFiles()
    GoOn = True
    while (GoOn):
        globalUserName = input("User Name: ")
        globalPassword = input("Password: ")
        if (ValidUser(globalUserName, globalPassword)):
            if(globalUserName.upper() == "ADMIN"):
                MenuAdmin()
                GoOn = False
            else:  
                MenuUser()
                GoOn = False
        else:
            print("\nInvalid User!\n")

#----------------------------------------------------------------    
def CreateDataFiles():
    import os
    if( not os.path.isfile("Accounts.txt")):
        AccountFile = open("Accounts.txt","w")
        AccountFile.close()
    if( not os.path.isfile("Transfer.txt")):
        Transfer = open("Transfer.txt","w")
        Transfer.close()

#----------------------------------------------------------------    
#Main
global globalUserName, globalPassword, globalAccountNo
globalUserName = ""   #In fact Same National Code
globalPassword = ""
globalAccountNo = "rrr"
Login()





 
