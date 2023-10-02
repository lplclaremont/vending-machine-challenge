class CoinBank:
    def __init__(self, coin_quantities):
        self.__check_quantities(coin_quantities.values())
        self.bank = {
            200: coin_quantities[200],
            100: coin_quantities[100],
            50: coin_quantities[50],
            20: coin_quantities[20],
            10: coin_quantities[10],
            5: coin_quantities[5],
            2: coin_quantities[2],
            1: coin_quantities[1]
        }
        self.deposited_funds = 0
    
    def deposit(self, coin_value):
        '''
        This function adds to deposited_funds and updates self.bank
        by incrementing the quantity of the corresponding coin
        value by one.

        Param:
        coin_value (int): value of coin in pence

        Returns:
        None

        '''

        self.__check_deposit_value(coin_value)
        self.bank[coin_value] += 1
        self.deposited_funds += coin_value

    def dispense_change(self, item_value):
        '''
        This function calculates the change (coins) to be returned
        and updates the self.bank quantities accordingly.

        Param:
        item_value (int): cost of item being purchased in pence

        Returns:
        Change as a list of coin values
        
        '''
        self.__check_item_value(item_value)

        customer_change = []
        remaining_change = self.deposited_funds - item_value
        for coin_value, quantity in self.bank.items():
            while remaining_change - coin_value >= 0 and quantity != 0:
                customer_change.append(coin_value)
                remaining_change -= coin_value
                quantity -= 1
            self.bank[coin_value] = quantity

        if remaining_change > 0:
            for coin in customer_change:
                self.bank[coin] += 1
            raise ValueError('Unable to dispence the correct change')
        
        return customer_change 

    def reset_funds(self):
        '''
        This resets the deposited_funds variable to zero.
        '''
        self.deposited_funds = 0 

    # Checking error cases
    def __check_quantities(self, quantities):
        for q in quantities:
            if type(q) != int or q < 0:
                raise TypeError('Coin quantities must be non negative integers')
    
    def __check_deposit_value(self, coin_value):
        valid_values = self.bank.keys()
        if coin_value not in valid_values:
            raise ValueError('Deposits must be a valid UK coin denomination')
        
    def __check_item_value(self, value):
        if type(value) != int or value < 0:
            raise TypeError('Item value must be a non negative integer')
        elif value > self.deposited_funds:
            raise ValueError('Deposit more funds')
        