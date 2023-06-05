"""This is the same coffee machine project as from day 15,
 except using classes."""
from day_16_menu import Menu
from day_16_coffee_maker import CoffeeMaker
from day_16_money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

should_continue = True

while should_continue is True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        should_continue = False
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) is True:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
