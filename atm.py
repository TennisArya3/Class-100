class Atm (object):
    def __init__(self,cardnum,pinnum):
        self.cardnum=cardnum
        self.pinnum=pinnum
    def CashWithdrawal (self):
        print("Cash has been withdrawn:")

    def Balance (self):
        print("Your balance is 1cr!")
P1=Atm("120345","56647")
P1.CashWithdrawal()
P1.Balance()