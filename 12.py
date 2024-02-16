"""
Exercise12 -> Create a Simple Get_coffee Class with coffee Types
"""


class Cafe:
    def __init__(self, money, coffee_type):
        self.money = money
        self.coffee_type = coffee_type

    def get_coffee(self):
        coffee_types = {
            "espresso": 3000,
            "latte": 5000,
            "milk": 4000,
            "lungo": 3500,
        }
        if self.coffee_type in coffee_types.keys():
            coffee_charge = coffee_types[self.coffee_type]
            if self.money < coffee_charge:
                print(f"Sorry! Your Budget is Low for {self.coffee_type}")
                print(f"You Need {coffee_charge - self.money} More!")
            else:
                change = self.money - coffee_charge
                print(f"Here's Your {self.coffee_type}!")
                print("And Your Change: ", change)
        else:
            print("Sorry, We Don't Have That!")


c2 = Cafe(10000, "milk")
c2.get_coffee()
