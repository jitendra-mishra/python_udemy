class BankAccount:
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def print_balance(self):
        print(f"Your current balance is {self.balance}")
    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Enter a valid amount")
    def make_withdraw(self, amount):
        if amount > self.balance:
            print("You don't have sufficient balance")
        else:
            self.balance -= amount

class SavingsBankAccount(BankAccount):
    INTEREST_RATES = 0.035
    def __init__(self, owner, balance, currency):
        BankAccount.__init__(self, owner, balance, currency)
        self.interest_rate = SavingsBankAccount.INTEREST_RATES
    def deposit_interest_earned(self):
        interest_earned = self.balance * SavingsBankAccount.INTEREST_RATES
        self.balance += interest_earned

class CheckingBankAccount(BankAccount):
    def __init__(self, owner, balance, currency, debit_card=None, credit_card=None):
        BankAccount.__init__(self, owner, balance, currency)
        self.debit_card = debit_card
        self.credit_card = credit_card

my_savings_account = SavingsBankAccount("Jitendra", 2000, "INR")
my_savings_account.print_balance()
my_savings_account.make_deposit(-10)
my_savings_account.print_balance()