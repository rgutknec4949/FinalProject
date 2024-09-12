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

    def check_resources(self, ingredients):
        bread_num = ingredients.get("bread")
        ham_num = ingredients.get("ham")
        cheese_num = ingredients.get("cheese")

        bread_have = self.machine_resources.get("bread")
        ham_have = self.machine_resources.get("ham")
        cheese_have = self.machine_resources.get("cheese")

        all_check = 0
        if bread_num <= bread_have:
            all_check += 1
        else:
            print("Sorry there is not enough bread")

        if ham_num <= ham_have:
            all_check += 1
        else:
            print("Sorry there is not enough ham")

        if cheese_num <= cheese_have:
            all_check += 1
        else:
            print("Sorry there is not enough cheese")

        if all_check == 3:
            return True
        else:
            return False

    def process_coins(self):
        money_have = 0.00

        print("\nPlease insert coins.")
        the_input = float(input("How many large dollars?: "))

        money_have = money_have + the_input

        the_input = float(input("How many half dollars?: "))

        money_have = money_have + (the_input * 0.50)

        the_input = float(input("How many quarters?: "))

        money_have = money_have + (the_input * 0.25)

        the_input = float(input("How many nickels?: "))

        money_have = money_have + (the_input * 0.25)

        return money_have

    def transaction_result(self, coins, cost):
        self.machine_resources = self.machine_resources
        if coins >= cost:
            change = coins - cost
            print(f"Here is : ${change:.2f} in change")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        bread_used = recipes[sandwich_size]["ingredients"]["bread"]
        self.machine_resources["bread"] -= bread_used

        ham_used = recipes[sandwich_size]["ingredients"]["ham"]
        self.machine_resources["ham"] -= ham_used

        cheese_used = recipes[sandwich_size]["ingredients"]["cheese"]
        self.machine_resources["cheese"] -= cheese_used

    def report_time(self):
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print("Ham: ", resources.get("ham"), " slice(s)")
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


