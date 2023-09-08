class VendingMachine:
    def __init__(self):
        self.coin_bank = {}
        self.deposited_funds = {}

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

    def __check_quantities(self, quantities):
        for q in quantities:
            if q < 0 or type(q) != int:
                raise TypeError('Coin quantities must be non negative integers')