class BankAccount:
    """
    Bank account information
    """
    def __init__(self,account_holder,balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def withdraw(self,fund):
        """
        Withdraw money from the balance
        """
        print(f"Withdrawing {fund} from {self.__account_holder}'s account")
        if fund>self.__balance:
            print(f"Insufficient funds to withdraw from {self.__account_holder}'s account")
        else:
            self.__balance -= fund
            print(f"Balance: {self.__balance}")

    def deposit(self,fund):
        """
        Deposit money into the balance
        """
        print(f"Depositing {fund} into {self.__account_holder}'s account")
        self.__balance += fund
        print(f"Balance: {self.__balance}")

    def account_information(self):
        """
        Print account information
        """
        print(f"{self.__account_holder}'s balance is currently {self.__balance}")

    # Getters
    @property
    def balance(self):
        """Balance"""
        return self.__balance

    @property
    def account_holder(self):
        """Account holder"""
        return self.__account_holder
    
my_account = BankAccount("Robert", 10000)
ken_account = BankAccount("Ken", 8000)
bob_account = BankAccount("Bob", 80)
my_account.withdraw(100)
my_account.deposit(800)
my_account.account_information()

bob_account.withdraw(1000)
