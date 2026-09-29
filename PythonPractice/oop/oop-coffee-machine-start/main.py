from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_variant = coffee_menu.find_drink(input(f'What would you like today {coffee_menu.get_items()}'))
if coffee_menu.find_drink(coffee_variant.name):
    if coffee_maker.is_resource_sufficient(coffee_variant):
        if money_machine.make_payment(coffee_variant.cost):
            coffee_maker.make_coffee(coffee_variant)

