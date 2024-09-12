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

TheMachine = SandwichMachine(resources)

input_check = 0

while (input_check == 0):
    user_input = input("What would you like to order today? (small/ medium/ large/ off/ report): ")
    if user_input == "small":
        The_Ingred = recipes["small"]["ingredients"]
        if TheMachine.check_resources(The_Ingred) == True:
            cost = recipes["small"]["cost"]
            money_have = TheMachine.process_coins()
            if TheMachine.transaction_result(money_have, cost) == True:
                TheMachine.make_sandwich("small", The_Ingred)
                print("Small sandwich is ready. Bon appetit!")
        else:
            print("Unfortunately, we cannot make this sandwich")
    elif (user_input == "medium"):
        The_Ingred = recipes["medium"]["ingredients"]
        if TheMachine.check_resources(The_Ingred) == True:
            cost = recipes["medium"]["cost"]
            money_have = TheMachine.process_coins()
            if TheMachine.transaction_result(money_have, cost) == True:
                TheMachine.make_sandwich("medium", The_Ingred)
                print("Medium sandwich is ready. Bon appetit!")
        else:
            print("Unfortunately, we cannot make this sandwich")

    elif (user_input == "large"):
        The_Ingred = recipes["large"]["ingredients"]
        if TheMachine.check_resources(The_Ingred) == True:
            cost = recipes["large"]["cost"]
            money_have = TheMachine.process_coins()
            if TheMachine.transaction_result(money_have, cost) == True:
                TheMachine.make_sandwich("large", The_Ingred)
                print("Large sandwich is ready. Bon appetit!")
        else:
            print("Unfortunately, we cannot make this sandwich")

    elif (user_input == "off"):
        print("You have turned off the machine. Good night.")
        input_check = 1
    elif (user_input == "report"):
        print("We currently have:")
        TheMachine.report_time()
    else:
        print("Oops! You have not chosen one of the options. Please choose one of the options")


