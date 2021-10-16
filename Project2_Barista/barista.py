class coffee_order:
    def __init__(self):
        '''Initalizes variables for coffee order.'''
        self.coffeeType = ""
        self.size = ""
        self.milk = "n"
        self.price = 0
    def errorMessage(self):
        '''Prints general error message when three tries are used up.'''
        print()
        print("Sorry, we cannot help you here!")
        print()
    def order_coffee(self):
        '''gives user three tries to give order else it breaks the loop'''
        self.continueDisplay = True
        tries = 0
        while True:
            print()
            print("Coffee Menu: Black, Latte, Iced Black, and Iced Latte")
            print("-----------------------------------------------------")
            '''asks user for coffee type'''
            self.coffeeType = input("What type of coffee would you like?: ")
            self.coffeeType = self.coffeeType.lower()
            if (self.coffeeType == "black" or self.coffeeType == "latte" 
            or self.coffeeType == "iced black" or self.coffeeType == "iced latte"):
                continueProgram = True
                if self.coffeeType == "black" or self.coffeeType == 'iced black':
                    newTries = 0
                    while True:
                        '''Asks user for milk or no milk if coffee type is black or iced black.'''
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
                        '''Asks user for size of coffee.'''
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
        '''puts prices table in a list'''
        if self.continueDisplay == True:
            pricesList = [1.25, 1.40, 2.00, 2.20, 0.05, 1.50, 1.90, 2.50, 2.70, 0.10, 1.75, 2.40, 3.00, 3.20, 0.20]
            '''Based on size or milk it offsets the position of n to retrieve the correct element.'''
            if self.size == 'short':
                n = 0
            elif self.size == 'regular':
                n = 5
            else:
                n = 10
            if self.coffeeType == 'black':
                if self.milk == 'y':
                    self.price = pricesList[0+n]+pricesList[4+n]
                else:
                    self.price = pricesList[0+n]
            if self.coffeeType == 'iced black':
                self.price = pricesList[1+n]
                if self.milk == 'y':
                    self.price = self.price+pricesList[4+n]
            if self.coffeeType == 'latte':
                self.price = pricesList[2+n]
            if self.coffeeType == 'iced latte':
                self.price = pricesList[3+n]
        self.price = format(self.price, '.2f')
        return self.price
    def __repr__(self):
        '''Displays the coffee order in required format using __repr__.'''
        if self.continueDisplay == True:
            display = ("Coffee Type: " + self.coffeeType.upper() + "\n" + "Coffee Size: " + self.size.upper() + "\n" 
            + "Milk Added: " + self.milk.upper() + "\n" + "Price: $" + str(self.price))
            return display
        else:
            return "No Order!"

personOrder1 = coffee_order()
personOrder1.order_coffee()
print()
print("Order Summary")
print("-----------------------------------------------------")
personOrder1.calc_price()
print(repr(personOrder1))
print("-----------------------------------------------------")
print()

'''Prints out Docstrings:'''
# print()
# print("Documentation: ")
# print("Using __init__():")
# print(personOrder1.__init__.__doc__)
# print()
# print("Using errorMessage():")
# print(personOrder1.errorMessage.__doc__)
# print()
# print("Using orderCoffee():")
# print(personOrder1.order_coffee.__doc__)
# print()
# print("Using calcPrice():")
# print(personOrder1.calc_price.__doc__)
# print()
# print("Using __repr__():")
# print(personOrder1.__repr__.__doc__)
# print()