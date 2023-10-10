import art
print(art.logo)
new_bidder = True

print("Welcome to the secret auction program.")

bids = {}
highest_bid = 0
while new_bidder:
    name = input("What is your name? \n")
    bid = int(input("What's your bid? \n"))

    if bid >= highest_bid:
        highest_bid = bid
        winner = name

    bids[name] = bid

    keep_going = True
    while keep_going:
        more_bidders = input("Are there any other bidders? Type 'Yes' or 'No'. \n").lower()
        if more_bidders == "no":
            new_bidder = False
            keep_going = False
        elif more_bidders == "yes":
            new_bidder = True
            keep_going = False
        else:
            print("That's not a valid option. Try Again.")

print(f"The winner of the auction is: {winner} paying", bids[winner], "bucks")




































