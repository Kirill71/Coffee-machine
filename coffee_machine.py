# water = 400
# milk = 540
# coffeeBeans = 120
# cups = 9
# money = 550


class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, cups, money=0):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"The coffee machine has:\n"\
               f"{self.water} of water\n"\
               f"{self.milk} of milk\n" \
               f"{self.coffee_beans} of coffee beans\n" \
               f"{self.cups} of disposible cups\n"\
               f"{self.money} of money\n"

    def make_coffee(self, coffee_type):
        if coffee_type == "1":
            self.__change_state(4, 250, 0, 16)
        elif coffee_type == "2":
            self.__change_state(7, 350, 75, 20)
        elif coffee_type == "3":
            self.__change_state(6, 200, 100, 12)
        else:
            pass

    def fill_coffee_machine(self, w, m, b, c):
        self.water += w
        self.milk += m
        self.coffee_beans += b
        self.cups += c

    def give_money(self):
        money = self.money
        self.money = 0
        return f"I gave you ${money}"

    def __change_state(self, price, w, m, b):
        if self.__can_make_coffee(1, w, m, b):
            self.money += price
            self.water -= w
            self.milk -= m
            self.coffee_beans -= b
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough {}!".format(self.__find_missing_component(1, w, m, b)))
        print()

    def __can_make_coffee(self, c, w, m, b):
        return self.cups - c >= 0 \
                and self.water - w >= 0 \
                and self.milk - m >= 0 \
                and self.coffee_beans - b >= 0

    def __find_missing_component(self, c, w, m, b):
        if self.cups - c < 0:
            return "cups"
        elif self.water - w < 0:
            return "water"
        elif self.milk - m < 0:
            return "milk"
        elif self.coffee_beans - b < 0:
            return "coffee beans"


def main():
    coffeeMachine = CoffeeMachine(water=400, milk=540, coffee_beans=120, cups=9, money=550)
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        op = input(">")
        if op == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            coffee_type = input(">")
            coffeeMachine.make_coffee(coffee_type)
        elif op == "fill":
            print("Write how many ml of water do you want to add:")
            w = int(input(">"))
            print("Write how many ml of milk do you want to add:")
            m = int(input(">"))
            print("Write how many grams of coffee beans do you want to add:")
            b = int(input(">"))
            print("Write how many disposable cups of coffee do you want to add:")
            c = int(input(">"))
            coffeeMachine.fill_coffee_machine(w, m, b, c)
        elif op == "take":
            print(coffeeMachine.give_money())
        elif op == "remaining":
            print(coffeeMachine)
            print()
        else:
            break


main()
