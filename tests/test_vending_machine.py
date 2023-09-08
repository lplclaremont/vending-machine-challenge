import pytest
from lib.vending_machine import VendingMachine

"""
A vending machine is initialised with
an empty coin bank and deposited funds
"""
def test_vending_machine_initialised():
    machine = VendingMachine()
    assert machine.coin_bank == {}
    assert machine.deposited_funds == 0

"""
#load_coins updates the coin_bank 
with correct quantitites when called
"""
def test_loading_coins():
    machine = VendingMachine()
    machine.load_coins(7,6,5,4,3,2,1,0)
    assert machine.coin_bank == {
        2: 7, 1: 6, 0.5: 5, 0.2: 4, 0.1: 3, 0.05: 2, 0.02: 1, 0.01: 0
    }

"""
#load_coins throws an error when the input
are not valid coin quantities
"""
def test_invalid_coin_quantity():
    machine = VendingMachine()
    with pytest.raises(TypeError) as err_info:
        machine.load_coins(-2, 1, 1, 1, 1, 1, 1, 1)
    assert str(err_info.value) == 'Coin quantities must be non negative integers'

"""
#deposit_coin updates deposited_funds
with correct coin when called
"""
def test_deposit_coin():
    machine = VendingMachine()
    machine.deposit(0.5)
    machine.deposit(0.2)
    assert machine.deposited_funds == 0.7

"""
#deposit_coin throws an error when
value is not a valid coin amount
"""
def test_invalid_deposit():
    machine = VendingMachine()
    with pytest.raises(ValueError) as err_info:
        machine.deposit(0.32)
    assert str(err_info.value) == 'Deposits must be a valid UK coin denomination'

"""
#get_change returns the correct coin quantities and removes
them from coin_bank based on item value and funds
when there are certainly enough coins in coin bank
"""
def test_no_change_given():
    machine = VendingMachine()
    machine.load_coins(20,20,20,20,20,20,20,20)
    machine.deposit(1)
    assert machine.get_change(1) == []

def test_one_coin_given_in_change():
    machine = VendingMachine()
    machine.load_coins(20,20,20,20,20,20,20,20)
    machine.deposit(1)
    assert machine.get_change(0.5) == [0.5]
    assert machine.coin_bank[0.5] == 19

def test_different_denominations_given():
    machine = VendingMachine()
    machine.load_coins(20,20,20,20,20,20,20,20)
    machine.deposit(2)
    assert machine.get_change(1.44) == [0.5, 0.05, 0.01]
    assert machine.coin_bank[0.5] == 19
    assert machine.coin_bank[0.05] == 19
    assert machine.coin_bank[0.01] == 19

def test_multiple_coins_same_denomination_given():
    machine = VendingMachine()
    machine.load_coins(20,20,20,20,20,20,20,20)
    machine.deposit(2)
    assert machine.get_change(1.6) == [0.2, 0.2]
    assert machine.coin_bank[0.2] == 18

def test_multiple_coins_and_diff_denominations_given():
    machine = VendingMachine()
    machine.load_coins(20,20,20,20,20,20,20,20)
    machine.deposit(2)
    machine.deposit(1)
    assert machine.get_change(1.59) == [1, 0.2, 0.2, 0.01]
    assert machine.coin_bank[1] == 19
    assert machine.coin_bank[0.2] == 18
    assert machine.coin_bank[0.01] == 19

"""
#get_change correctly returns change when one denomination
in coin_bank runs out and removes them from coin_bank
"""
def test_multiple_coins_and_diff_denominations_given():
    machine = VendingMachine()
    machine.load_coins(1,20,20,20,20,20,20,20)
    machine.deposit(2)
    machine.deposit(2)
    machine.deposit(0.2)
    assert machine.get_change(0.2) == [2, 1, 1]
    assert machine.coin_bank[2] == 0
    assert machine.coin_bank[1] == 18

"""
#get_change throws an error if the required coins
for change all go to zero
"""
def test_error_when_out_of_coins():
    machine = VendingMachine()
    with pytest.raises(ValueError) as err_info:
        machine.load_coins(0,0,0,0,0,0,0,1)
        machine.deposit(0.05)
        machine.get_change(0.03)
    assert str(err_info.value) == 'Unable to dispence the correct change, contact customer support'

"""
#reset_funds resets the deposited funds to zero
"""
def test_reset_funds():
    machine = VendingMachine()
    machine.deposit(2)
    assert machine.deposited_funds == 2
    machine.reset_funds()
    assert machine.deposited_funds == 0

