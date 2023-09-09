# Vending Machine Change Tracker

## Overview
This API is to be used in conjunction with vending machine software in order to track the coins inside the machine. It is to be set initially with the given quantities of each denomination and then will be updated as the user makes deposits and purchases.

## Design
My work includes just one class, since we are only handling the behaviour change of the quantities of coins inside the machine. This is all kept inside the CoinBank class.
Instances of CoinBank are initialised with a list of quantities of coin denominations (£2, £1, 50p, 20p, 10p, 5p, 2p, 1p) and also the value of coins deposited by a user. So the input parameter is a python list with 8 integers, and the deposited funds is initially set to zero. The coins inside the machine are stored in a class variable called self.bank, which is a dictionary with coin values (in pence) as keys and their quantities as values. This allows us to handily keep track of and update the quantity of each denomination and also use their monetary value for calculations.

There are three main methods on the CoinBank class:

**deposit:** This method allows users to deposit coins, one by one, into the machine and they will be added to the coin bank. I've made the assumption that coins the user deposits are available for the machine to dispense as change, so the method updates the bank dictionary.

**dispense_change:** This method takes one parameter (the item's value to be purchased) and calculates the coins required as change based on the current funds deposited and the coin quantities in the bank dictionary. The bank dictionary is updated as required (coins returned as change are removed from the bank) and the method returns a list of the coins to be given to a user.

**reset_funds:** This method sets the deposited funds variable back to zero. Once a purchase is made, reset_funds can be called to reset funds back to zero.

#### Notes on design choices
These decisions have been made when implementing the API:
- I have used pence for the coin values (i.e £1 = 100, 50p = 50) to remove all risk of float rounding errors in calculations.
- I have only allowed the deposit method to take one parameter (i.e, one coin) since the vending machine will only have one coin inputted at a time.
- I have kept reset_funds in a seperate method in order to ensure that dispense_change *only* handles the behaviour of finding the change. We could also imagine a scenario in which the funds are incorrect due to a fault in the hardware of the vending machine, and it must be reset back to zero manually.
- The deposited funds is just stored as the total value of coins deposited so far, since for this exercise we only require the total value in order to calculate the change.
- The dispense_change return value is a list of the coin values, as this can be easily iterated through in another part of the software in order to tell the machine which coins to remove from the machine.

#### Edge cases
I have implemented errors with appropriate messages for the following cases:
- If the coin quantities when initialising a CoinBank instance aren't all integers >= 0.
- The value passed into the deposit method is not a valid UK coin denomination (or not an integer).
- The value passed into the dispense_change method is not a valid monetary amount (integer > 0).
- The item's value in the dispense_change method is greater than the amount that the user has deposited.
- The bank has run out of the right coin denominations in order to dispense the total amount of change necessary.

### Setup and Use

```bash
# clone the repository and cd into it
git clone https://github.com/lplclaremont/vending-machine-challenge
cd vending-machine-challenge

# use brew to install pyenv in order to install dependencies
brew install pyenv

pipenv install
```

You can import and use the class now as follows in a python file:
```python
from path-to-'vending-machine-challenge'.lib.coin_bank import CoinBank
# quantities of coins in order --> [£2, £1, 50p, 20p, 10p, 5p, 2p, 1p]
coin_quantities = [20,20,20,20,20,20,20,20]

coin_bank = CoinBank(coin_quantities)

# deposit coins
coin_bank.deposit(20)   # 20p coin added
coin_bank.deposit(100)   # £1 coin added
print(coin_bank.deposited_funds)
# --> 120 (£1.20)

# get change for item purchase
change = coin_bank.dispense_change(105)  # item price --> £1.05
print(change)
# --> [10, 5] (10 pence and 5 pence coins)

# return deposited funds to 0
coin_bank.reset_funds()
print(coin_bank.deposited_funds)
# --> 0
```