WATER = 300
MILK = 200
COFFEE = 100
MONEY = 0

water = 300
milk = 200
coffee = 100
money = 0
machines_money = 0

machine_on = True
money_inserted = 0
money_inserted2 = "{:.2f}".format(money_inserted)

while machine_on:
    question_which_beverage = True
    print(f"\n${money_inserted2} currently in machine.\n")

    done_ordering = False

    while not done_ordering:
        question_which_beverage = True

        while question_which_beverage:
            chosen_beverage_input = input("What would you like? (E:espresso / L:latte / C:cappuccino): ").lower()

            if chosen_beverage_input == "r" or chosen_beverage_input == "report":
                chosen_beverage = "report"
                print(f"\nMATERIALS:\nWATER: {water}ml\nMILK: {milk}ml\nCOFFEE: {coffee}\nMONEY: ${("{:.2f}".format(machines_money))}\n")
                continue_asking_refill = True 

                while continue_asking_refill:
                    if water == WATER and milk == MILK and coffee == COFFEE and machines_money == MONEY:
                        print("Machine is full of all materials.")
                        
                    refill_machine = input("Would you like to refill the machine? 'Y' or 'N': ").lower()
                    if refill_machine == "y" or refill_machine == "yes":
                        keep_refilling = True
                        while keep_refilling:
                            refill_what_material = input("What would you like to refill? 'W', 'M', 'C': ").lower()

                            if water == WATER and milk == MILK and coffee == COFFEE and machines_money == MONEY:
                                print("Machine is full of all materials.")
                                print("REFILL ENDED")
                                continue_asking_refill = False
                                keep_refilling = False
                            elif refill_what_material == "money":
                                if machines_money > MONEY:
                                    print(f"You have removed ${("{:.2f}".format(machines_money))} from the machine.")
                                    print(f"Money remianing in machine: ${MONEY}")
                                    machines_money = 0
                                else:
                                    print("There is no money in the machine to remove.")
                            elif refill_what_material == "w" or refill_what_material == "water":
                                if water < WATER:
                                    water_needed = WATER - water
                                    print(f"You added {water_needed}ml of water.")
                                    print(f"Water remaining in machine: {WATER}ml")
                                    water = WATER
                                else:
                                    print("The water in the machine is already full.")
                            elif refill_what_material == "m" or refill_what_material == "milk":
                                if milk < MILK:
                                    milk_needed = MILK - milk
                                    print(f"You added {milk_needed}ml of milk.")
                                    print(f"Milk remaining in machine: {MILK}ml")
                                    milk = MILK
                                else:
                                    print("The milk in the machine is already full.")
                            elif refill_what_material == "c" or refill_what_material == "coffee":
                                if coffee < COFFEE:
                                    coffee_needed = COFFEE - coffee
                                    print(f"You added {coffee_needed}g of coffee.")
                                    print(f"Coffee remaining in machine: {COFFEE}g")
                                    coffee = COFFEE
                                else:
                                    print("The coffee in the machine is already full.")
                                    keep_refilling = False
                            elif refill_what_material == "s" or refill_what_material == "stop" or refill_what_material == "d" or refill_what_material == "done":
                                print("REFILL ENDED")
                                keep_refilling = False
                            else:
                                print("Invalid entry.")

                    elif refill_machine == "n" or refill_machine == "no":
                        continue_asking_refill = False
                    else: 
                        print("Invalid entry.")

            elif chosen_beverage_input == "e" or chosen_beverage_input == "espresso":
                chosen_beverage = "espresso"
                print(chosen_beverage.lower())
                question_which_beverage = False
            elif chosen_beverage_input == "l" or chosen_beverage_input == "latte":
                chosen_beverage = "latte"
                print(chosen_beverage.lower())
                question_which_beverage = False
            elif chosen_beverage_input == "c" or chosen_beverage_input == "cappuccino":
                chosen_beverage = "cappuccino"
                print(chosen_beverage.lower())
                question_which_beverage = False
            elif chosen_beverage_input == "o" or chosen_beverage_input == "off":
                chosen_beverage = "off"
                question_which_beverage = False
                done_ordering = True
                machine_on = False
            else:
                print("Invalid entry.")

            check_machine_for_materials = True

            while check_machine_for_materials:
                if chosen_beverage == "espresso":
                    water_needed = 50
                    milk_needed = 0
                    coffee_needed = 18
                    water_remaining = water - water_needed
                    milk_remaining = milk - milk_needed
                    coffee_remaining = coffee - coffee_needed
                elif chosen_beverage == "latte":
                    water_needed = 200
                    milk_needed = 150
                    coffee_needed = 24
                    water_remaining = water - water_needed
                    milk_remaining = milk - milk_needed
                    coffee_remaining = coffee - coffee_needed
                elif chosen_beverage == "cappuccino":
                    water_needed = 250
                    milk_needed = 100
                    coffee_needed = 24
                    water_remaining = water - water_needed
                    milk_remaining = milk - milk_needed
                    coffee_remaining = coffee - coffee_needed
                elif chosen_beverage == "off" or chosen_beverage == "report":
                    water_needed = 0
                    milk_needed = 0
                    coffee_needed = 0
                    water_remaining = water - water_needed
                    milk_remaining = milk - milk_needed
                    coffee_remaining = coffee - coffee_needed

                    check_machine_for_materials = False
                    add_money = False
                    money_left_over = False

                if water_remaining < 0:
                    print(f"There is not enough water in the machine to make the {chosen_beverage}.")
                    print("Please pick a different beverage.")
                    water_remaining += water_needed
                    check_machine_for_materials = False
                elif milk_remaining < 0:
                    print(f"There is not enough milk in the machine to make the {chosen_beverage}.")
                    print("Please pick a different beverage.")
                    milk_remaining += milk_needed
                    check_machine_for_materials = False
                elif coffee_remaining < 0:
                    print(f"There is not enough coffee in the machine to make the {chosen_beverage}.")
                    print("Please pick a different beverage.")
                    coffee_remaining += coffee_needed
                    check_machine_for_materials = False
                elif water_remaining >= 0 and milk_remaining >= 0 and coffee_remaining >= 0: 
                    check_machine_for_materials = False
                    question_which_beverage = False
                    done_ordering = True

    water = water_remaining
    milk = milk_remaining
    coffee = coffee_remaining

    add_money = True

    while add_money:
        if chosen_beverage == "espresso":
            cost_of_item = 1.50
            cost_of_item_str = "1.50"
        elif chosen_beverage == "latte":
            cost_of_item = 2.50
            cost_of_item_str = "2.50"
        elif chosen_beverage == "cappuccino":
            cost_of_item = 3.00
            cost_of_item_str = "3.00"
        else:
            cost_of_item = 0
            cost_of_item_str = "0.00"

        if money_inserted < cost_of_item:
            adding_money = float(input(f"{(chosen_beverage).upper()} is ${cost_of_item_str}. Insert cash or card: $"))
            money_inserted += adding_money

        machines_money += cost_of_item

        need_more_money = True

        while need_more_money:
            if money_inserted < cost_of_item:
                money_needed_still = cost_of_item - money_inserted
                money_needed_still2 = "{:.2f}".format(money_needed_still)
                add_more_money = float(input(f"You are ${money_needed_still2} short. Please add more money: $"))
                money_inserted += add_more_money
            else:
                need_more_money = False
                add_money = False

    if chosen_beverage == "report":
        print("Done with report.")
    elif chosen_beverage == "off":
        print()
    else:
        print(f"Here is your {chosen_beverage}.")

    money_inserted -= cost_of_item
    money_inserted2 = "{:.2f}".format(money_inserted)

    money_left_over = True

    while money_left_over:
        if money_inserted > 0:
            buy_more = input(f"You have ${money_inserted2} remaining. Would you like to buy another beverage or get change? (B:beverage / C:change): ").lower()
            if buy_more in ("c", "change"):
                print(f"Here is your change: ${money_inserted2}")
                money_left_over = False
                money_inserted = 0
                money_inserted2 = "{:.2f}".format(money_inserted)
            else:
                money_left_over = False
        else:
            money_left_over = False

    money = float("{:.2f}".format(money_inserted))
    MONEY = int(money)

print("POWER OFF")