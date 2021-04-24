class CoffeeMachine:
    COFFEE_INGREDIENTS = {
        'espresso': {
            'water': 250,
            'milk': 0,
            'coffee_beans': 16,
            'disposal_cups_amount': 1,
            'money': -4,
        },
        'latte': {
            'water': 350,
            'milk': 75,
            'coffee_beans': 20,
            'disposal_cups_amount': 1,
            'money': -7,
        },
        'cappuccino': {
            'water': 200,
            'milk': 100,
            'coffee_beans': 12,
            'disposal_cups_amount': 1,
            'money': -6,
        },
    }

    def __init__(self, water, milk, coffee_beans, disposal_cups, money):
        self.coffee_machine_supplies = {
            'water': water,  # ml
            'milk': milk,  # ml
            'coffee_beans': coffee_beans,  # g
            'disposal_cups_amount': disposal_cups,
            'money': money,  # dollars
        }

    def user_action_interface(self, chosen_action):
        actions = {
            'buy': lambda: self._choose_coffee(
                input("What do you want to buy? "
                      "1 - espresso, "
                      "2 - latte, "
                      "3 - cappuccino, "
                      "back - to main menu:")),
            'fill': lambda: self._fill_supplies(
                int(input("Write how many ml of water do you want to add:")),
                int(input("Write how many ml of milk do you want to add:")),
                int(input("Write how many grams of coffee beans do you want to add:")),
                int(input("Write how many disposable cups of coffee do you want to add:")),
            ),
            'take': self._take_money_action,
            'remaining': self._print_remaining_supplies,
        }

        return actions[chosen_action]()

    def _choose_coffee(self, chosen_coffee_number):
        if chosen_coffee_number == 'back':
            return False

        coffee_numbers = {
            '1': 'espresso',
            '2': 'latte',
            '3': 'cappuccino',
        }

        return self._take_supplies_for_coffee(
            coffee_numbers[chosen_coffee_number]
        )

    def _fill_supplies(self, water, milk, coffee, disposal_cups):
        self.coffee_machine_supplies['water'] \
            += water
        self.coffee_machine_supplies['milk'] \
            += milk
        self.coffee_machine_supplies['coffee_beans'] \
            += coffee
        self.coffee_machine_supplies['disposal_cups_amount'] \
            += disposal_cups

    def _take_money_action(self):
        taken_money = self.coffee_machine_supplies['money']
        self.coffee_machine_supplies['money'] = 0
        print(f"I gave you ${taken_money}")

    def _print_remaining_supplies(self):
        print(f"""The coffee machine has:
    {self.coffee_machine_supplies['water']} of water
    {self.coffee_machine_supplies['milk']} of milk
    {self.coffee_machine_supplies['coffee_beans']} of coffee beans
    {self.coffee_machine_supplies['disposal_cups_amount']} of disposable cups
    {self.coffee_machine_supplies['money']} of money""")

    def _is_enough_supply_check(self, chosen_coffee):
        for ingredient in self.COFFEE_INGREDIENTS[chosen_coffee]:
            if self.coffee_machine_supplies[ingredient] \
                    < self.COFFEE_INGREDIENTS[chosen_coffee][ingredient]:
                print(f"Sorry, not enough {ingredient}!")
                return False

        print("I have enough resources, making you a coffee!")
        return True

    def _take_supplies_for_coffee(self, chosen_coffee):
        if self._is_enough_supply_check(chosen_coffee):
            for ingredient in self.COFFEE_INGREDIENTS[chosen_coffee]:
                self.coffee_machine_supplies[ingredient] \
                    -= self.COFFEE_INGREDIENTS[chosen_coffee][ingredient]
