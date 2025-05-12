class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        while True:
            user_input = input('''
            1. Press 1 to create PIN
            2. Press 2 to make a withdrawal
            3. Press 3 to check balance
            4. Press 4 to exit
            Enter your choice: ''')
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.withdrawal()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid input. Please try again.")
    def create_pin(self):
        new_pin = input("Enter your new PIN: ")
        new_balance = int(input("Enter your starting balance: "))
        self.pin = new_pin
        self.balance = new_balance
        print("PIN created successfully!")
    def withdrawal(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. New balance is: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN.")
    def check_balance(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Incorrect PIN.")
x1=Atm()