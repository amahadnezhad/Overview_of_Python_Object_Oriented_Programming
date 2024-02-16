"""
Exercise10 -> Create a Simple Get_coffee Class
"""


class Cafe:
    def __init__(self, money):
        self.money = money

    def get_coffee(self):
        coffee_charge = 5000
        if self.money < coffee_charge:
            print("Sorry! Your Budget is Low!")
            print(f"You Need {coffee_charge-self.money} More!")
        else:
            change = self.money - coffee_charge
            print("Here's Your Coffee!")
            print("And Your Change: ", change)


c1 = Cafe(10000)
c1.get_coffee()
