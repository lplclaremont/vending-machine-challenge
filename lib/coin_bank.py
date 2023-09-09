class CoinBank:
    def __init__(self, coin_quantities):
        self.__check_quantities(coin_quantities)
        self.bank = {
            200: coin_quantities[0],
            100: coin_quantities[1],
            50: coin_quantities[2],
            20: coin_quantities[3],
            10: coin_quantities[4],
            5: coin_quantities[5],
            2: coin_quantities[6],
            1: coin_quantities[7]
        }
        self.deposited_funds = 0
    
    def deposit(self, coin_value):
        self.__check_deposit_value(coin_value)
        self.bank[coin_value] += 1
        self.deposited_funds += coin_value

    def dispense_change(self, item_value):
        self.__check_item_value(item_value)

        coins_for_change = []
        remaining_change = self.deposited_funds - item_value
        for coin_value, quantity in self.bank.items():
            while remaining_change - coin_value >= 0 and quantity > 0:
                coins_for_change.append(coin_value)
                remaining_change -= coin_value
                quantity -= 1
            self.bank[coin_value] = quantity

        if sum(coins_for_change) < (self.deposited_funds - item_value):
            raise ValueError('Unable to dispence the correct change, contact customer support')
        
        return coins_for_change 

    def reset_funds(self):
        self.deposited_funds = 0 

    def __check_quantities(self, quantities):
        for q in quantities:
            if type(q) != int or q < 0:
                raise TypeError('Coin quantities must be non negative integers')
    
    def __check_item_value(self, value):
        if type(value) != int or value <= 0:
            raise TypeError('Item value must be a positive integer')
        elif value > self.deposited_funds:
            raise ValueError('Deposit more funds')
        
    def __check_deposit_value(self, coin_value):
        valid_values = [200, 100, 50, 20, 10, 5, 2, 1]
        if coin_value not in valid_values:
            raise ValueError('Deposits must be a valid UK coin denomination')
        