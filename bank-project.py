
# import logging
# logging.basicConfig(
#     filename="app.log",
#     filemode='w',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# class ATM:
#     def __init__(self , balance =0 ):
#         self.balance = balance 

#         def check_balance (self):
#             logging.info("Balanace Checked")

#         def deposit(self , amount):
#             if amount > 0:
#                 self.balance += amount 
#                 logging.info(f"Deposited: ${amount}")

#             else:
#                 logging.warning("Invalid deposit amount")

#         def withdraw(self , amount):
#             if 0 < amount <= self.balance:
#                 self.balance -= amount 
#                 logging.info(f"Withdrawn: ${amount}")
#             else:
#                 logging.warning("Withdrawal failed due to insufficient funds or invalid amount")

        
import logging

# Basic logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            logging.error(f"Deposit failed: Negative amount {amount} for {self.holder}")
            raise ValueError("Amount must be positive.")
        self.balance += amount
        logging.info(f"Deposit of {amount} to {self.holder} completed.")

    def withdraw(self, amount):
        if amount > self.balance:
            logging.error(f"Withdrawal failed: Not enough balance for {self.holder}")
            raise ValueError("Not enough balance.")
        self.balance -= amount
        logging.info(f"Withdrawal of {amount} from {self.holder} completed.")

    def get_balance(self):
        return self.balance

def perform_transactions(account):
    try:
        account.deposit(-50)
    except Exception as e:
        print("Deposit Error:", e)

    try:
        account.withdraw(1000)
    except Exception as e:
        print("Withdrawal Error:", e)

    try:
        account.deposit(200)
    except Exception as e:
        print("Deposit Error:", e)

    try:
        account.withdraw(50)
    except Exception as e:
        print("Withdrawal Error:", e)

# Run example
acc = BankAccount("Alice", 100)
perform_transactions(acc)
print("Final Balance:", acc.get_balance())
