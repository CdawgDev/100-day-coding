import gavel
import os

clear = lambda: os.system('cls')
print(gavel.logo)
print("Welcome to the secret auction program")

program_running = True
auction_bidders = {}


def start_auction():
  name = input("What is your name?: ")
  bid = int(input("What is your bid amount? $"))
  auction_bidders[name] = bid
  more_bids = input("Is there more bidders yes or no: ")
  if more_bids == "no":
    temp_count = 0
    for item in auction_bidders:
      if auction_bidders[item] > temp_count:
        temp_count = auction_bidders[item]
        highest_bidder = item
    print(f"The winner is {highest_bidder} with a bid of ${temp_count}")
    return ()
  else:
    clear()
    start_auction()


start_auction()
