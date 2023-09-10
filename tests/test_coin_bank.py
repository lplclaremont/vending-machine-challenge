import pytest
from lib.coin_bank import CoinBank

"""
A coin bank is initialised with 
the correct coin quantities from parameters
"""
def test_initially():
    coin_bank = CoinBank([7,6,5,4,3,2,1,0])
    assert coin_bank.bank == {
        200: 7, 100: 6, 50: 5, 20: 4, 10: 3, 5: 2, 2: 1, 1: 0
    }

"""
Throws an error when the initial input
are not all valid coin quantities
"""
def test_invalid_coin_quantity():
    with pytest.raises(TypeError) as err_info:
        coin_bank = CoinBank([-2, 1, 1, 1, 1, 1, 1, 1])
    assert str(err_info.value) == 'Coin quantities must be non negative integers'

"""
#deposit_coin updates deposited_funds
and coin_bank with correct coin when called
"""
def test_deposit_coin():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(50)
    coin_bank.deposit(20)
    assert coin_bank.deposited_funds == 70
    assert coin_bank.bank[50] == 21
    assert coin_bank.bank[20] == 21

"""
#deposit_coin throws an error when
value is not a valid coin amount
"""
def test_invalid_deposit():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    with pytest.raises(ValueError) as err_info:
        coin_bank.deposit(32)
    assert str(err_info.value) == 'Deposits must be a valid UK coin denomination'


"""
#dispense_change returns the correct coin quantities and removes
them from coin_bank based on item value and funds
when there are certainly enough coins in coin bank
"""
def test_no_change_given():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(100)
    assert coin_bank.dispense_change(100) == []

def test_one_coin_given_in_change():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(100)
    assert coin_bank.dispense_change(50) == [50]
    assert coin_bank.bank[50] == 19

def test_different_denominations_given():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(200)
    assert coin_bank.dispense_change(144) == [50, 5, 1]
    assert coin_bank.bank[50] == 19
    assert coin_bank.bank[5] == 19
    assert coin_bank.bank[1] == 19

def test_multiple_coins_same_denomination_given():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(200)
    assert coin_bank.dispense_change(160) == [20, 20]
    assert coin_bank.bank[20] == 18

def test_multiple_coins_and_diff_denominations_given():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(200)
    coin_bank.deposit(100)
    assert coin_bank.dispense_change(159) == [100, 20, 20, 1]
    assert coin_bank.bank[100] == 20
    assert coin_bank.bank[20] == 18
    assert coin_bank.bank[1] == 19

"""
#dispense_change correctly returns change when one denomination
in coin_bank runs out and removes them from coin_bank
"""
def test_multiple_coins_and_diff_denominations_given():
    coin_bank = CoinBank([20,20,20,1,20,20,20,20])
    coin_bank.deposit(100)
    assert coin_bank.dispense_change(60) == [20, 10, 10]
    assert coin_bank.bank[20] == 0
    assert coin_bank.bank[10] == 18

def test_complicated_example():
    coin_bank = CoinBank([20,20,10,1,3,0,1,4])
    coin_bank.deposit(200)
    coin_bank.deposit(100)
    assert coin_bank.dispense_change(124) == [100, 50, 20, 2, 1, 1, 1, 1]
    assert coin_bank.bank[2] == 0

"""
#dispense_change throws an error if the required coins
for change all go to zero
"""
def test_error_when_out_of_coins():
    coin_bank = CoinBank([0,0,0,0,0,0,0,1])
    coin_bank.deposit(5)
    with pytest.raises(ValueError) as err_info:
        coin_bank.dispense_change(3)
    assert str(err_info.value) == 'Unable to dispence the correct change, contact customer support'

"""
#dispense_change throws an error if the item value
if not valid money value
"""
def test_invalid_item_value():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(10)
    with pytest.raises(TypeError) as err_info:
        coin_bank.dispense_change(-10)
    assert str(err_info.value) == 'Item value must be a non negative integer'


"""
#dispense_change returns the total deposited
funds if the item_value is zero
"""
def test_zero_item_value():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(200)
    coin_bank.deposit(50)
    assert sum(coin_bank.dispense_change(0)) == 250

"""
#dispense_change raises an error if item_value is
higher than the total amount deposited
"""
def test_not_enough_funds():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    with pytest.raises(ValueError) as err_info:
        assert coin_bank.dispense_change(10)
    assert str(err_info.value) == 'Deposit more funds'
    assert coin_bank.bank == {200: 20, 100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20 }


"""
#reset_funds resets the deposited funds to zero
"""
def test_reset_funds():
    coin_bank = CoinBank([20,20,20,20,20,20,20,20])
    coin_bank.deposit(200)
    assert coin_bank.deposited_funds == 200
    coin_bank.reset_funds()
    assert coin_bank.deposited_funds == 0

