auction_names = {}


def auction():
    auction_name = input("Enter the name of the bidder:")
    auction_price = int(input("Enter the price of the bid:"))
    auction_names[auction_name] = auction_price
    should_continue = input("Are there any other bidders? Type Y or N:")
    if should_continue == "N":
        return
    else:
        auction()


max_price = 0
winner = ""
auction()
for auction in auction_names:
    if auction_names[auction] > max_price:
        max_price = auction_names[auction]
        winner = auction

print(f"The winner is {winner} with a bid of ${max_price}.")
