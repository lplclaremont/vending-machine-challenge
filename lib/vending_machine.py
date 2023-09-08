# This is required since we will encounter errors with float arithmetic
# from decimal import Decimal as D

class VendingMachine:
    def __init__(self):
        self.coin_bank = {}
        self.deposited_funds = 0

    def load_coins(self, two_pounds, pounds, fifties, twenties, tens, fives, twos, ones):
        quantities = [two_pounds, pounds, fifties, twenties, tens, fives, twos, ones]
        self.__check_quantities(quantities)

        self.coin_bank[200] = two_pounds
        self.coin_bank[100] = pounds
        self.coin_bank[50] = fifties
        self.coin_bank[20] = twenties
        self.coin_bank[10] = tens
        self.coin_bank[5] = fives
        self.coin_bank[2] = twos
        self.coin_bank[1] = ones
    
    def deposit(self, coin_value):
        self.__check_deposit_value(coin_value)
        self.deposited_funds += coin_value

    def get_change(self, item_value):
        coins_for_change = []
        change_value = self.deposited_funds - item_value
        for coin, quantity in self.coin_bank.items():
            coin_value = coin
            while change_value - coin_value >= 0 and quantity > 0:
                coins_for_change.append(coin)
                change_value -= coin_value
                quantity -= 1
            self.coin_bank[coin] = quantity

        if sum(coins_for_change) < (self.deposited_funds - item_value):
            raise ValueError('Unable to dispence the correct change, contact customer support')
        
        return coins_for_change
    
    def reset_funds(self):
        self.deposited_funds = 0
    

    def __check_quantities(self, quantities):
        for q in quantities:
            if type(q) != int or q < 0:
                raise TypeError('Coin quantities must be non negative integers')
    
    def __check_deposit_value(self, coin_value):
        valid_values = [200, 100, 50, 20, 10, 5, 2, 1]
        if coin_value not in valid_values:
            raise ValueError('Deposits must be a valid UK coin denomination')