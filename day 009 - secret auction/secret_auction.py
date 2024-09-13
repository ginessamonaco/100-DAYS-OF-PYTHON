name_bid_dict = {}


complete = False

while not complete:
    end = False
    x = 0

    while not end: 
        done = False

        while not done:
            print(f"Start the bid at ${x}.")
            name = input("What is your name?: ")
            bid = int(input("What is your bid?: $"))

            valid_bid = False

            while not valid_bid:
                if bid < x:
                    print(f"\nBid higher than ${x}.")
                    bid = int(input("What is your bid?: $"))
                else:
                    valid_bid = True

            name_bid_dict[name] = bid

            other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
            if other_bidders == "no":
                done = True
            else:
                print("\n" * 100)

        key_list = list(name_bid_dict.keys())
        value_list = list(name_bid_dict.values())

        finally_list = []
        name1 = ""
        x = 0

        for d in name_bid_dict:
            if name_bid_dict[d] >= x:
                x = name_bid_dict[d]
                name1 = d

        position = value_list.index(x)
        stop = False
        multiple_winners = False

        while not stop:
            for o in name_bid_dict:
                if name_bid_dict[o] == x:
                    if o != name1:
                        multiple_winners = True
                        reveal = input(f"\nMultiple people chose to bid ${x}. Type 'yes' to reveal their names, type 'no' to restart the bid at ${x}.\n").lower()
                        if reveal == "yes":
                            for n in name_bid_dict:
                                if name_bid_dict[n] == x:
                                    print(f"{n} had a bid of {x}.")
                            stop = True
                            end = True
                            complete = True
                        elif reveal == "no":
                            stop = True
                else:
                    stop = True

        if not multiple_winners:
                print(f"\nThe winner is {(key_list[position]).upper()} with a bid of ${x}.")
                end = True
                complete = True

print("Bid session over.\n")
