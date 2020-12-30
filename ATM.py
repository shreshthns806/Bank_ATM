# Create a class named ATM
class ATM:
    
    # Define its properties
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
    
    # Create a function to enquire about balance
    def balance_enquiry(self):

        print("You have chosen to enquire about balance.")
        cancel = input("If you wish to cancel, type cancel. If you don't want to cancel, type anything else. ")

        # Handle if user wants to continue
        if(cancel != "cancel"):
            print("Your balance is- "+ str(self.balance))
            startup()
        
        # Handle if user wishes to exit
        else:
            startup()
    
    # Create a function to withdraw cash
    def cash_withdrawl(self):
        
        print("You have chosen to withdraw cash.")
        cancel = input("If you wish to cancel, type cancel. If you don't want to cancel, type anything else. ")


        # Handle if user wants to continue
        if(cancel != "cancel"):
            
            # Ask the user for amount to be withdrawn
            amount_to_be_withdrawn = int(input("[Enter only integer values] How much money do you want to withdraw? "))
            
            # Handle if amount to be withdrawn is less than or equal to available balance
            if(amount_to_be_withdrawn <= self.balance):
                self.balance = self.balance - amount_to_be_withdrawn
                print("Transaction Succesful!")
                startup()
            
            # Handle if amount to be withdrawn is greater than available balance
            else:
                print("The amount you wish to withdraw is greater than your balance! Please try again with a lower value.")
                self.cash_withdrawl()
        
        # Handle if user wishes to exit
        else:
            startup()


# Create a function to launch at startup
def startup():

    # Ask the user what action he wants to do.
    method_input = int(input("Welcome to Shreshth Bank! Type 1 for balance enquiry and 2 for cash withdrawl. Type 0 to exit. "))

    # Handle if user wants to enquire about balance
    if method_input == 1:
        my_account.balance_enquiry()
    
    # Handle if user wants to withdraw cash
    elif method_input == 2:
        my_account.cash_withdrawl()
    
    # Handle if user wants to exit
    elif method_input == 0:
        exit()
    
    # Handle if value doesn't match any other value in the options given
    else:
        print("ERROR! Try Again")
        startup()

my_account = ATM(123456, 123456, 10000)

# Ask the user for card number and PIN
input_card_number = int(input("Enter Card Number Here: "))
input_pin = int(input("Enter your PIN here: "))

# Handle if PIN and card number are correct
if(input_pin == my_account.pin and input_card_number == my_account.card_number):
    startup()
        
# Handle if wrong password is entered
else:
    print("Wrong PIN or Card Number!")
    exit()