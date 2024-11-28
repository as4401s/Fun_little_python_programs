from os import system
import platform

print('Welcome to Blind Auction!')

bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    winner = ''
    highest_bid = 0
    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The highest bidder is {winner} and the bid amount is ${highest_bid}')

while continue_bidding:

    name = input('What is your name? : ')
    price = int(input('What is your bid? : $'))

    bids[name] = price
    
    more_people = input('Are there more people? (yes/no): ').lower()
    
    if more_people == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
        
    if more_people == 'yes':
        # Clear screen for next user, depending on OS
        if platform.system() == 'Windows':
            system('cls')
        else:
            system('clear')

        
    
    

