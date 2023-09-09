from lib.coin_bank import CoinBank
print("")
print("Test out the coin storage API as follows:")
print("We'll set up an initial state of 20 coins of each denomination in the machine.")
print("Now you can view the total coins in the machine,")
print("deposit funds (one coin at a time) and see the change when purchasing an item.")
print("")
print("Enter 'peek' to see the total coins,")
print("'deposit' to deposit a coin")
print("and 'purchase' to see the change given with an order")
print("type 'exit' to finish testing")
print("")
coin_bank = CoinBank([20,20,20,20,20,20,20, 20])

while True:
    print("'peek': see coins")
    print("'deposit': add coin")
    print("'purchase': see change given")
    print("'exit' to quit")

    response = input()
    if response == 'peek':
        print(coin_bank.bank)
        
    elif response == 'purchase':
        print("Enter value of item to buy (in pence)")
        print("i.e., £2.50 = 250, 79p = 79")
        print("Note -- deposited funds: ", coin_bank.deposited_funds)
        item_value = int(input())
        try:
            print("Change received: ", coin_bank.dispense_change(item_value))
            coin_bank.reset_funds()
        except Exception as error:
            print("An exception occurred: ", error)
    
    elif response == 'deposit':
        print("Enter a coin to deposit (in pence)")
        print("i.e, £1 = 100, 20p = 20, 1p = 1")
        coin = int(input())
        try:
            coin_bank.deposit(coin)
            print("New total funds: ", coin_bank.deposited_funds)
        except Exception as error:
            print("An exception occurred:", error)
    elif response == 'exit':
        break
    print(" ")






