from lib.vending_machine import VendingMachine

"""
A vending machine is initialised with
an empty coin bank and deposited funds
"""
def test_vending_machine_initialised():
    machine = VendingMachine()
    assert machine.coin_bank == {}
    assert machine.deposited_funds == {}
