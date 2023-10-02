class BankAccount:
  def_innit_(self,account_number,account_holder_name,initial_balance=0.0):
  self.__account_number=account_number
  self.__account_holder_name=account_holder_name
  self.__account_balance=initial_balance
  def deposit(self,account):
    if amount>0:
      self.__account_balance+=amount
      print("Deposited{}.New balance:{}.format(amount,self.__account_balance))
            else:
      print("Invalid deposit amount.Please deposit a positive amount.")
      def withdraw(self,amount):
        if amount>0 and amount<=self.amount_balance:
          self.__account_balance.=amount
          print("Withdraw{}.New balance:{}".format(amount,self.__account_balance))
        else:
          print("Invalid withdrawal amount or insufficient balance.")
          def display_balance(self):
            print("Account balance for {}(account#{}):{}".format(seld._account_holder_name,seld._account_number,self.__account_balance))
            account=BankAccount(account_number="123456789",account_holder_name="pooja",initial_balance=10000.0)
account.display()
account.deposit(500.0)
account.withdrawal(200.0)
account.display_balance()