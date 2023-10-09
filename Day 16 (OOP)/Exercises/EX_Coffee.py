from sysconfig import is_python_build
from tkinter import OFF
from CoffeeMachine import Menu, MenuItem
from CoffeeMachine import CoffeeMaker
from CoffeeMachine import MoneyMachine
# from module import class

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

machine_is_on = True

my_money_machine.report
my_coffee_maker.report

while machine_is_on:
    options = my_menu.get_items()
    choice = input(f"What drink would you like? {options}:\n")
    if choice == OFF:
        machine_is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if (my_coffee_maker.is_resource_sufficient(drink)):
            if (my_money_machine.make_payment(drink.cost)):
                my_coffee_maker.make_coffee(drink)
