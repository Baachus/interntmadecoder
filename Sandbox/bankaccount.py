class BankAccount:
    """
    Bank account information
    """
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self,fund):
        """
        Withdraw money from the balance
        """
        print(f"Withdrawing {fund} from {self.account_holder}'s account")
        if fund>self.balance:
            print(f"Insufficient funds to withdraw from {self.account_holder}'s account")
        else:
            self.balance -= fund
            print(f"Balance: {self.balance}")

    def deposit(self,fund):
        """
        Deposit money into the balance
        """
        print(f"Depositing {fund} into {self.account_holder}'s account")
        self.balance += fund
        print(f"Balance: {self.balance}")

    def account_information(self):
        """
        Print account information
        """
        print(f"{self.account_holder}'s balance is currently {self.balance}")


my_account = BankAccount("Robert", 10000)
ken_account = BankAccount("Ken", 8000)
bob_account = BankAccount("Bob", 80)
my_account.withdraw(100)
my_account.deposit(800)
my_account.account_information()

bob_account.withdraw(1000)
