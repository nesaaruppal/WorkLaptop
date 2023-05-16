from sysconfig import is_python_build
from tkinter import OFF
from Classes_Coffee import Menu
from Classes_Coffee import CoffeeMaker
from Classes_Coffee import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_maker.report()
money_machine.report()

machine_is_on = True

while machine_is_on:
    options = menu.get_items()
    choice = input(f"Which drink would you like {options}?\n")
    if choice == OFF:
        machine_is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink)):
            if(money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)
