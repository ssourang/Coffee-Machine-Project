from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#TODO: Create objects
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

wants_coffee = True
while wants_coffee:
    options = my_menu.get_items()
    choice = input(f'What would you like? ({options}):')
    if choice == 'off':
        wants_coffee = False
    elif choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        is_enough_ingredients = my_coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = my_money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            my_coffee_maker.make_coffee(drink)
                




