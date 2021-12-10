############### Blackjack Project #####################

############### Our Blackjack House Rules ####################

## The deck is unlimited in size. 
## There are no jokers. Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

########### Setup Code ##############

import random

dealer_cards = []
player_cards = []

##################### Functions #####################

def draw_card(side):
    """Returns random card from the deck"""
    random_card = random.choice(cards)
    if random_card == 11:
        side.append(random_card)
        if sum(side) > 21:
            #side.index(11) = 1 returns: SyntaxError: can't assign to function call
            side.pop()
            side.append(1)
        else:
            return
    side.append(random_card)

def init_cards():
    """Populates the initial array of cards for dealer and player"""
    for n in range(2):
        draw_card(dealer_cards)
        draw_card(player_cards)

def player_draw():
    """Puts player in a loop asking if they want to draw a card"""
    loop = True
    print(f'Your cards: {player_cards}, current score: {sum(player_cards)}')
    while loop == True:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
            draw_card(player_cards)
        else:
            loop = False
    
    blackjack_check(player_cards)

def dealer_draw():
    """Makes sure dealer's score is not less than 17"""
    while sum(dealer_cards) < 17:
        draw_card(dealer_cards)
        blackjack_check(dealer_cards)
        
def blackjack_check(side):
    """Checks if the side given has a blackjack"""
    if sum(side) == 21:
        return 0
    
def who_won(player_score, dealer_score):
    """Determines the winning side"""
    if player_score > dealer_score:
        print('You win')
    elif player_score < dealer_score:
        print('You lose')
    else:
        print('It\'s a draw')

def show_score(condition, player, dealer):
    """Shows user the score based on the condition"""
    if condition == 'normal':
        player_hand = "Your cards"
        dealer_hand = "first card"
        final = ""
    elif condition == 'final':
        player_hand = "final_hand"
        dealer_hand = player_hand
        final = f', final score: {sum(dealer_cards)}'
    
    print(f'Your {player_hand}: {player_cards}, current score: {sum(player_cards)}')
    print(f'Computer\'s {dealer_hand}: {dealer_cards[0]}{final}')

##################### Main Program #####################

def play_game():
    """Blackjack application function"""
    playing = True
    while playing:
        new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if new_game == 'y':
            # populate the dealer and player cards
            init_cards()
            show_score('normal', player_cards, dealer_cards)
            if sum(dealer_cards) < 17:
                dealer_draw()
            if player_draw() == 0:
                show_score('final', player_cards, dealer_cards)
                print("You have a Blackjack, You won!")
                play_game()
            elif blackjack_check(dealer_cards) == 0:
                show_score('final', player_cards, dealer_cards)
                print("Dealer has BlackJack, You  lost")
                play_game()
            else:
                show_score('final', player_cards, dealer_cards)
                who_won(sum(player_cards), sum(dealer_cards))
                play_game()
        # start of the game
        elif new_game == 'n':
            playing = False
            
##################### Calling Program #####################

play_game()
