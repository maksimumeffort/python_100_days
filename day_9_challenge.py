print('Welcome to a silent auction')
still_running = True
bid_log = {}

def get_highest_bid():
    highest_bid = 0
    highest_bidder = ''
    
    for key in bid_log:
        if bid_log[key] > highest_bid:
            highest_bid = bid_log[key]
            highest_bidder = key
    
    
    print(f"The highest bidder was {highest_bidder} with a bid of {highest_bid}")
        

while still_running:
    name = input("What is your name?\n").capitalize()
    bid = int(input('What is your bid?\n'))

    bid_log[name] = bid

    more_bids = input('Are there any more bidders? Type "yes" or "no"\n').lower()
    if more_bids == "no":
        get_highest_bid()
        still_running = False
  
  

