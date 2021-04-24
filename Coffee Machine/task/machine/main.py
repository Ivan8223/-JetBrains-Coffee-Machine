from custom_coffee_machine import CoffeeMachine


def main():
    user_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

    while True:
        user_action = input("Write action (buy, fill, take, remaining, exit):")

        if user_action == 'exit':
            break

        user_coffee_machine.user_action_interface(user_action)


if __name__ == '__main__':
    main()
