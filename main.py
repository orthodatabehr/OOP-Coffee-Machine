from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


turn_off = False
new_cm = CoffeeMaker()
new_mm = MoneyMachine()
new_menu = Menu()
while not turn_off:
    order_input = input(f'Please choose a drink {new_menu.get_items()}: ')
    if order_input == 'off':
        turn_off = True
    elif order_input == 'report':
        new_cm.report()
        new_mm.report()
    else:
        order = new_menu.find_drink(order_input)
        if order:
            if new_cm.is_resource_sufficient(order):
                if new_mm.make_payment(order.cost):
                    new_cm.make_coffee(order)
                    new_cm.report()
                    new_mm.report()

