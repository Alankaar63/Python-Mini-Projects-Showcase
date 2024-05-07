#Personal Budget Tracker
class Budget():
    def __init__(self, income, rent, ent, utilities, groceries, transportation):
        self.income = income
        self.rent = rent
        self.ent = ent
        self.utilities = utilities
        self.groceries = groceries
        self.transportation = transportation

    def display(self):
        print(f"Your monthly income is {self.income} rupees")
        print(f'Total expenses: {self.expenses()} rupees')
        print(f"Your annual income: {self.income2(200000, 12)} rupees")  # Call income2 with grosspay and months_worked

    def expenses(self):
        return self.rent + self.ent + self.utilities + self.groceries + self.transportation

    def income2(self, grosspay, months_worked):  # Pass grosspay and months_worked as arguments
        total_income = (grosspay / months_worked) * 12
        return total_income

    @staticmethod
    def income_1(grosspay, months_worked):
        return Budget(grosspay, 0, 0, 0, 0, 0)

    @staticmethod
    def expenses_1(rent, ent, utilities, groceries, transportation):
        print("This is your expense:")
        return Budget(0, rent, ent, utilities, groceries, transportation)

    def __sub__(self, other):
        if isinstance(other, Budget):
            total_savings = self.income - other.expenses()
            return total_savings
        else:
            print("Error 404: Please try again!")

TI = Budget.income_1(200000, 12)
TE = Budget.expenses_1(4000, 1200, 800, 1600, 2000)

print("Total Income:")
TI.display()

print("\nTotal Expenses:")
TE.display()

TS = TI - TE
print(f'Your total saving is: {TS} rupees')



