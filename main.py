### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    # Checks if machine has enough ingredients to create sandwich
    def check_resources(self, ingredients):

        # Gets the amount of bread needed for the sandwich
        bread_num = ingredients.get("bread")

        # Gets the amount of ham needed for the sandwich
        ham_num = ingredients.get("ham")

        # Gets the amount of cheese needed for the sandwich
        cheese_num = ingredients.get("cheese")

        # Gets the amount of bread the machine currently has
        bread_have = self.machine_resources.get("bread")

        # Gets the amount of ham the machine currently has
        ham_have = self.machine_resources.get("ham")

        # Gets the amount of cheese the machine currently has
        cheese_have = self.machine_resources.get("cheese")

        # This variable is to check how many ingredients are
        # sufficient to make the sandwich
        all_check = 0

        # Checks to see if the machine has enough bread to make sandwich
        if bread_num <= bread_have:
            # Machine has enough bread and adding 1 to all_check
            all_check += 1
        else:
            # Letting the user know that there is not enough bread
            print("Sorry there is not enough bread")

        # Checks to see if the machine has enough ham to make sandwich
        if ham_num <= ham_have:
            # Machine has enough ham and adding 1 to all_check
            all_check += 1
        else:
            # Letting the user know that there is not enough ham
            print("Sorry there is not enough ham")

        # Checks to see if the machine has enough cheese to make sandwich
        if cheese_num <= cheese_have:
            # Machine has enough cheese and adding 1 to all_check
            all_check += 1
        else:
            # Letting the user know that there is not enough cheese
            print("Sorry there is not enough cheese")

        # If all_check is three, it means that all ingredients are
        # sufficient to make the sandwich, resulting in returning True
        if all_check == 3:
            return True
        # If at least one ingredient is insufficient to make the sandwich
        # resulting in returning False
        else:
            return False

    # Calculates coins that was inputted into the machine
    def process_coins(self):

        # Initializes how much the user has before they input any coins
        money_have = 0.00

        # Asks the user to input coins
        print("\nPlease insert coins.")

        # Asking the user how many large dollars they want to input
        the_input = float(input("How many large dollars?: "))

        # Adding the amount of large dollars they have to their input
        money_have = money_have + the_input

        # Asking the user how many half dollars they want to input
        the_input = float(input("How many half dollars?: "))

        # Adding the amount of half dollars they have to their input
        # along with calculating the half dollars by multiplying 0.5 to the input
        money_have = money_have + (the_input * 0.50)

        # Asking the user how many quarters they want to input
        the_input = float(input("How many quarters?: "))

        # Adding the amount of quarters they have to their input
        # along with calculating the quarters by multiplying 0.25 to the input
        money_have = money_have + (the_input * 0.25)

        # Asking the user how many nickels they want to input
        the_input = float(input("How many nickels?: "))

        # Adding the amount of nickels they have to their input
        # along with calculating the quarters by multiplying 0.05 to the input
        money_have = money_have + (the_input * 0.05)

        # Returning the total amount of money the user has inputted
        return money_have

    # Checks if money inputted into machine was enough for the cost of the sandwich
    def transaction_result(self, coins, cost):

        # If the user has inputted enough coins to cover the cost
        # of the sandwich
        if coins >= cost:

            # Calculating the change to give to the user
            change = coins - cost

            # Letting the user know how much change they have received
            print(f"Here is : ${change:.2f} in change")

            # Returning True since the coins were enough to cover the cost
            return True

        # If the user did not input enough to cover the cost of the sandwich
        else:

            # Letting the user know that they didn't input enough money to
            # buy the sandwich and that they were refunded
            print("Sorry that's not enough money. Money refunded.")

            # Returning True since the coins were enough to cover the cost
            return False

    # Takes away needed resources to make sandwich
    def make_sandwich(self, sandwich_size, order_ingredients):

        # Putting the amount of bread needed to be used into the bread_used variable
        bread_used = recipes[sandwich_size]["ingredients"]["bread"]

        # Subtracts the amount of bread needed to the amount
        # of bread the machine currently has
        self.machine_resources["bread"] -= bread_used

        # Putting the amount of ham needed to be used into the ham_used variable
        ham_used = recipes[sandwich_size]["ingredients"]["ham"]

        # Subtracts the amount of ham needed to the amount
        # of ham the machine currently has
        self.machine_resources["ham"] -= ham_used

        # Putting the amount of cheese needed to be used into the cheese_used variable
        cheese_used = recipes[sandwich_size]["ingredients"]["cheese"]

        # Subtracts the amount of cheese needed to the amount
        # of cheese the machine currently has
        self.machine_resources["cheese"] -= cheese_used

    # Reports on how much bread, ham, and cheese the machine has
    def report_time(self):

        # Printing the amount of bread the machine currently has
        print(f"Bread: {self.machine_resources['bread']} slice(s)")

        # Printing the amount of ham the machine currently has
        print("Ham: ", resources.get("ham"), " slice(s)")

        # Printing the amount of cheese the machine currently has
        print("Cheese: ", resources.get("cheese"), " pound(s)")

### Make an instance of SandwichMachine class and write the rest of the codes ###

# Created SandwichMachine instance
TheMachine = SandwichMachine(resources)

# This variable is created to exit the while loop when needed
input_check = 0

while (input_check == 0):

    # Asking the user to input one of the options provided
    user_input = input("What would you like to order today? (small/ medium/ large/ off/ report): ")

    # If the user has inputted "small"
    if user_input == "small":

        # Putting the amount of ingredients to make a small sandwich
        # into the The_Ingred variable
        The_Ingred = recipes["small"]["ingredients"]

        # If the machine has enough ingredients to make the small sandwich
        if TheMachine.check_resources(The_Ingred) == True:

            # Putting the cost of a small sandwich into the cost variable
            cost = recipes["small"]["cost"]

            # Calculating the amount of money the user has inputted
            money_have = TheMachine.process_coins()

            # If the user has inputted enough money to afford a small sandwich
            if TheMachine.transaction_result(money_have, cost) == True:

                # Makes the small sandwich using the ingredients needed for a small sandwich
                TheMachine.make_sandwich("small", The_Ingred)

                # Letting the user know that the machine has made the small sandwich
                print("Small sandwich is ready. Bon appetit!")

        # The machine does not have enough ingredients to make the small sandwich
        else:

            # Letting the user know that the machine cannot make the sandwich
            print("Unfortunately, we cannot make this sandwich")

    # If the user has inputted "medium"
    elif (user_input == "medium"):

        # Putting the amount of ingredients to make a medium sandwich
        # into the The_Ingred variable
        The_Ingred = recipes["medium"]["ingredients"]

        # If the machine has enough ingredients to make the medium sandwich
        if TheMachine.check_resources(The_Ingred) == True:

            # Putting the cost of a medium sandwich into the cost variable
            cost = recipes["medium"]["cost"]

            # Calculating the amount of money the user has inputted
            money_have = TheMachine.process_coins()

            # If the user has inputted enough money to afford a medium sandwich
            if TheMachine.transaction_result(money_have, cost) == True:

                # Makes the medium sandwich using the ingredients needed for a medium sandwich
                TheMachine.make_sandwich("medium", The_Ingred)

                # Letting the user know that the machine has made the medium sandwich
                print("Medium sandwich is ready. Bon appetit!")

        # The machine does not have enough ingredients to make the medium sandwich
        else:

            # Letting the user know that the machine cannot make the sandwich
            print("Unfortunately, we cannot make this sandwich")

    # If the user has inputted "large"
    elif (user_input == "large"):

        # Putting the amount of ingredients to make a large sandwich
        # into the The_Ingred variable
        The_Ingred = recipes["large"]["ingredients"]

        # If the machine has enough ingredients to make the large sandwich
        if TheMachine.check_resources(The_Ingred) == True:

            # Putting the cost of a large sandwich into the cost variable
            cost = recipes["large"]["cost"]

            # Calculating the amount of money the user has inputted
            money_have = TheMachine.process_coins()

            # If the user has inputted enough money to afford a large sandwich
            if TheMachine.transaction_result(money_have, cost) == True:

                # Makes the large sandwich using the ingredients needed for a large sandwich
                TheMachine.make_sandwich("large", The_Ingred)

                # Letting the user know that the machine has made the large sandwich
                print("Large sandwich is ready. Bon appetit!")

        # The machine does not have enough ingredients to make the large sandwich
        else:

            # Letting the user know that the machine cannot make the sandwich
            print("Unfortunately, we cannot make this sandwich")

    # If the user has inputted the "off" option
    elif (user_input == "off"):

        # Lets the user know that they have turned off the machine
        print("You have turned off the machine. Good night.")

        # Making input_check 1 to exit the while loop
        input_check = 1

    # If the user has inputted the "report" option
    elif (user_input == "report"):

        # The machine currently has...
        print("We currently have:")

        # This prints what ingredients the machine currently has
        TheMachine.report_time()

    # If the user has not inputted one of the options
    else:

        # This lets the user know that they have not entered one of the options
        # and since input_check is still 0, the while loop still runs
        print("Oops! You have not chosen one of the options. Please choose one of the options")


