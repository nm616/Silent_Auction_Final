from replit import clear
from art import logo

print(logo)

stop_bids = False
bidders = {}

def find_winner():
  winner = ""
  high_bid = 0
  for key in bidders:
    bid_amount = bidders[key]
    if int(bid_amount) > int(high_bid):
      high_bid = bidders[key]
      winner = key
  print(f"The winner of the auction is {winner} with a bid of {high_bid}!")

while not stop_bids:
  name = input("Please Enter Your Name: ")
  bid = input("Please Enter Your Bid: $")
  bidders[name] = bid
  stop = input("Are there more bidders? Type 'yes' or 'no': ")
  if stop == "no":
    stop_bids = True
    clear()
    print(logo)
  elif stop == "yes":
    clear()

find_winner()