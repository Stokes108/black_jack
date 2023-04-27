'''
    How to improve this make a player class (parent) then a dealer class with a deck 
    Create a game class that handles both player and dealer - ie list of players- specific for each game
    imporve deck complexity - real deck
    

    create other game classes- black_jack, texas hold em, five card draw
    random inputs from computer 

    

'''



from random import shuffle

class Card():

    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
    
    def show_card(self):
        print(f'{self.value} of {self.suite}')


    
    
class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.cards = []

    def create_deck(self):

        suites = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for i in suites:
            for x in range(13):
                c = Card(i, x+1)
                self.cards.append(c)
        
        shuffle(self.cards)

        return self.cards

    
    def show_hand(self):
        print('')
        print(f"This is {self.name}'s hand: ")
        for x in self.hand:
            x.show_card()
    

    def show_deck(self):
        for x in range(len(self.cards)):
            self.cards[x].show_card()

    def remove_card(self):
        return self.cards.pop().show_card()

    def return_deck(self):
        return self.cards

    def hit(self, card):
        self.hand.append(card)

    def check_value(self):
        counter = 0

        for x in self.hand:
            counter += x.value
        
        return counter

        




    
def inital_deal(dealer, human_player):
    dealer.create_deck()

    dealer.hand = dealer.cards[-2:]
    dealer.cards.pop()
    dealer.cards.pop()



    card1 = dealer.cards.pop()
    card2 = dealer.cards.pop()

    human_player.hit(card1)
    human_player.hit(card2)

    dealer_val = dealer.check_value()
    player_val = human_player.check_value()


    
    if player_val == 21:
        return 'blackjack'    



    

    

def verify_yn(value):
    value_flag = True
    while value_flag:
        if value in 'yn':
            value_flag = False
        else:
            value = input("You did not enter y or n. Please choose again: ")
    return True if value == 'y' else False


def verify_hit(value):
    value_flag = True
    while value_flag:
        if value in 'hs':
            value_flag = False
        else:
            value = input("You did not enter h or s. Please choose again: ")
    return True if value == 'h' else False

def check_bust(player):
    player_value = player.check_value()

    if player_value > 21:
        return True


def finish_game(dealer, player):
    dealer_value = dealer.check_value()
    player_value = player.check_value()

    if (check_bust(dealer) and check_bust(player)) or player_value == dealer_value:
        return 'Game Tied'
    elif check_bust(player) and dealer_value <= 21:
        return 'Dealer Wins'
    elif player_value <= 21 and check_bust(dealer):
        return f'{player.name} Wins'
    elif player_value <= 21 and dealer_value <= 21 and player_value > dealer_value:
        return f'{player.name} Wins'
    elif player_value <= 21 and dealer_value <= 21 and player_value < dealer_value:
        return 'Dealer Wins'

def reset_deck(player, dealer):
    player.hand = []
    dealer.hand = []


def main():

    decision = verify_yn(input('Would you like to play black jack? (y/n)'))
    name = input('Please enter your name: ')

    dealer = Player('House')
    player = Player(name)
    marker = False

    while decision:
        if player.hand == []:
            check_bj = inital_deal(dealer, player)
            if check_bj:
                print(f"Blackjack! {player.name} you win!!!!")
                decision = verify_yn(input('Would you like to continue playing black jack? (y/n)'))

            else:

                player.show_hand()
                hit_decsion = verify_hit(input('Would you like to hit or stand? (h/s)'))
                while hit_decsion:
                    player.hit(dealer.cards.pop())
                  
                    player.show_hand()
                    if check_bust(player):
                        print('')
                        print(f'{player.name} you busted')
                        decision = verify_yn(input('You got busted would you like to play black jack again? (y/n)'))
                        reset_deck(dealer, player)
                        break
                    else:
                        hit_decsion = verify_hit(input('Would you like to hit or stand? (h/s)'))
                
                if player.hand != []:
                    print("The dealer's hand was: ")
                    dealer.show_hand()
                    print("Your hand was: ")
                    player.show_hand()
                    print(finish_game(dealer, player))
                    reset_deck(player, dealer)
                    decision = verify_yn(input('Would you like to continue playing black jack? (y/n)'))


    print("\nThank you for playing with us today!")




main()


        




''' 
    make a player class 
        name 
        hand - cards in a list 

        take a card

    Make a dealer class inheirted from player
        name 
        hand 
        deck 

        deal a card- intial 
        deal a card- after player takes 

'''    

