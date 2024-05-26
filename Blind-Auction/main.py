from replit import clear

from art import logo
print(logo)

bidder_list = {}

def add_bidder(bidder_name, bidder_price):
  bidder_list[bidder_name] = bidder_price
more_user = 'yes' 
should_continue = True
while should_continue:
  
  if more_user.lower() == 'yes':
    clear()
    name = input("What is the name of the bidder? \n")
    bid_price = int(input("What is your bid price? \n$"))
    add_bidder(name, bid_price)
    clear()
    more_user = input("Are there any other bidders? Type 'yes' or 'no'. \n")

  elif more_user.lower() == 'no':
    should_continue = False
    highest_bid = 0
    for bidder in bidder_list:
      if bidder_list[bidder] > highest_bid:
        highest_bid = bidder_list[bidder]
        winner = bidder
    clear()
    print(f"The winner is {winner} with a bid of ${highest_bid}.")