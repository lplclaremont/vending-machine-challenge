import pytest
from lib.vending_machine import VendingMachine

"""
A vending machine is initialised with
an empty coin bank and deposited funds
"""
def test_vending_machine_initialised():
    machine = VendingMachine()
    assert machine.coin_bank == {}
    assert machine.deposited_funds == {}

"""
Coin bank is updated with correct
quantitites when #load_coins method is called
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