def main():
    balance = 0
    cardNumber = int(input("Enter Your Card Number :- "))
    pinNumber = int(input("Enter Your Pin :- "))
    cn = 12345678
    pn = 123456

    print("Enter Respective no for Enquiry")
    print("0.Check Your Balance 1.Withdraw Money 2.Deposit Money")
    number = int(input("Enter No :- "))

    if (cardNumber == cn, pinNumber == pn):
        if (number == 0):
            print("Your Balance is Rs."+str(balance))

        elif (number == 1):
            withdrawMoney = int(input("Amount To Be Withdraw :- Rs."))
            if(balance > withdrawMoney):
                balance -= withdrawMoney
                print("Withdraw Success \n Current Balance is Rs."+str(balance))
            else:
                print("Transaction error! \n Your current balance is less than the withdraw amount!! \n Current balance is only Rs."+str(balance)+"!!!")
      
        elif(number == 2):
            depositMoney = int(input("Amount to be deposited :- Rs."))
            balance += depositMoney
            print("Deposit Success \n Current Balance is Rs."+str(balance))

    else:
        print("Wrong card number or password please enter again \n ")
        cardNumber = int(input("Enter Your Card Number"))
        pinNumber = int(input("Enter Your Pin"))

main()