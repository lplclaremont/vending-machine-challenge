# This is required since we will encounter errors with float arithmetic
from decimal import Decimal as D

class VendingMachine:
    def __init__(self):
        self.coin_bank = {}
        self.deposited_funds = 0

    def load_coins(self, two_pounds, pounds, fifties, twenties, tens, fives, twos, ones):
        quantities = [two_pounds, pounds, fifties, twenties, tens, fives, twos, ones]
        self.__check_quantities(quantities)

        self.coin_bank[2] = two_pounds
        self.coin_bank[1] = pounds
        self.coin_bank[0.5] = fifties
        self.coin_bank[0.2] = twenties
        self.coin_bank[0.1] = tens
        self.coin_bank[0.05] = fives
        self.coin_bank[0.02] = twos
        self.coin_bank[0.01] = ones
    
    def deposit(self, coin_value):
        self.__check_deposit_value(coin_value)
        self.deposited_funds += coin_value

    def get_change(self, item_value):
        coins_for_change = []
        change_value = D(str(self.deposited_funds)) - D(str(item_value))
        for coin, quantity in self.coin_bank.items():
            coin_value = D(str(coin))
            while change_value - coin_value >= 0 and quantity > 0:
                coins_for_change.append(coin)
                change_value -= coin_value
                quantity -= 1
            self.coin_bank[coin] = quantity
        return coins_for_change
    
    def reset_funds(self):
        self.deposited_funds = 0
    

    def __check_quantities(self, quantities):
        for q in quantities:
            if type(q) != int or q < 0:
                raise TypeError('Coin quantities must be non negative integers')
    
    def __check_deposit_value(self, coin_value):
        valid_values = [2, 1, 0.5, 0.2, 0.10, 0.05, 0.02, 0.01]
        if coin_value not in valid_values:
            raise ValueError('Deposits must be a valid UK coin denomination')