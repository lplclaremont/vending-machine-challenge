class VendingMachine:
    def __init__(self):
        self.coin_bank = {}
        self.deposited_funds = 0

    def load_coins(self, two_pound, pound, fifty, twenty, ten, five, two, one):
        quantities = [two_pound, pound, fifty, twenty, ten, five, two, one]
        self.__check_quantities(quantities)

        self.coin_bank[2] = two_pound
        self.coin_bank[1] = pound
        self.coin_bank[0.5] = fifty
        self.coin_bank[0.2] = twenty
        self.coin_bank[0.1] = ten
        self.coin_bank[0.05] = five
        self.coin_bank[0.02] = two
        self.coin_bank[0.01] = one
    
    def deposit(self, coin_value):
        self.__check_deposit_value(coin_value)
        self.deposited_funds += coin_value

    def __check_quantities(self, quantities):
        for q in quantities:
            if q < 0 or type(q) != int:
                raise TypeError('Coin quantities must be non negative integers')
    
    def __check_deposit_value(self, coin_value):
        valid_values = [2, 1, 0.5, 0.2, 0.10, 0.05, 0.02, 0.01]
        if coin_value not in valid_values:
            raise ValueError('Deposits must be a valid UK coin denomination')