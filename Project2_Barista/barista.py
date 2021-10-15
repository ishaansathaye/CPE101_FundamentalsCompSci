class coffee_order:
    def __init__(self):
        self.coffeeType = ""
        self.size = ""
        self.milk = "n"
    def errorMessage(self):
        print()
        print("Sorry, we cannot help you here!")
        print()
    def order_coffee(self):
        self.continueDisplay = True
        tries = 0
        while True:
            print()
            print("Coffee Menu: Black, Latte, Iced Black, and Iced Latte")
            print("-----------------------------------------------------")
            self.coffeeType = input("What type of coffee would you like?: ")
            self.coffeeType = self.coffeeType.lower()
            if self.coffeeType == "black" or self.coffeeType == "latte" or self.coffeeType == "iced black" or self.coffeeType == "iced latte":
                continueProgram = True
                if self.coffeeType == "black" or self.coffeeType == 'iced black':
                    newTries = 0
                    while True:
                        self.milk = input("Would you like milk on the side? (Y or N): ")
                        self.milk = self.milk.lower()
                        if self.milk == 'y' or self.milk == 'yes':
                            self.milk = "y"
                            break
                        elif self.milk == 'n' or self.milk == 'no':
                            self.milk = "n"
                            break
                        else:
                            newTries = newTries + 1
                            if newTries == 3:
                                self.errorMessage()
                                self.continueDisplay = False
                                continueProgram = False
                                break
                            else:
                                print()
                                print("Can you please try again?")
                if continueProgram == True:
                    sizeTries = 0
                    while True:
                        self.size = input("What size would you like? (Short, Regular, or Large): ")
                        self.size = self.size.lower()
                        if self.size == 'short' or self.size == 'regular' or self.size == 'large':
                            break
                        else:
                            sizeTries = sizeTries + 1
                            if sizeTries == 3:
                                self.errorMessage()
                                self.continueDisplay = False
                                break
                            else:
                                print()
                                print("Can you please try again?")
                break
            else:
                tries = tries + 1
                if tries == 3:
                    self.errorMessage()
                    self.continueDisplay = False
                    break
                else:
                    print()
                    print("Can you please try again?")
    def calc_price(self):
        pass
    def __repr__(self):
        if self.continueDisplay == True:
            display = "Coffee Type: " + self.coffeeType.upper() + "\n" + "Coffee Size: " + self.size.upper() + "\n" + "Milk Added: " + self.milk.upper() + "\n" + "Price:"
            return display
        else:
            return "No Order!"
    

personOrder1 = coffee_order()
personOrder1.order_coffee()
print()
print("Order Summary")
print("-----------------------------------------------------")
print(repr(personOrder1))
print()
