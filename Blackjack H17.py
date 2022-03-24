#Fully Functional Blackjack Program
#Dealer must hit soft 17, late surrender allowed, 8 deck
import random


#money class for player's cash flow
class Wallet:
    def __init__(self, amount = 0):
        self.__cash = amount

    def add(self, amount):
        self.__cash += amount

    def subtract(self, amount):
        self.__cash -= amount

    def is_empty(self):
        return self.__cash == 0

    def get_balance(self):
        return self.__cash

    
    

#card objects
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        string = f'{self.suit}, {self.value}'
        return string

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    #changes ace from 11 to 1 when necessary
    def ace_change(self):
        self.value = 1

    def ace_reverse(self):
        self.value = 11

    def is_ace(self):
        if self.value == 11:
            return True
        else:
            return False

    def is_ace2(self):
        if self.value == 1:
            return True
        else:
            return False
        


#deck object, store cards here, create card types, draw cards
#internal deck list used as stack
class Deck:
    def __init__(self):
        self.cards = {'Ace of Spades' : 11, '2 of Spades' : 2, '3 of Spades' : 3,
            '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
            '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
            '10 of Spades' : 10, 'Jack of Spades' : 10,
            'Queen of Spades' : 10, 'King of Spades' : 10, 'Ace of Hearts' : 11,
            '2 of Hearts' : 2, '3 of Hearts' : 3, '4 of Hearts' : 4,
            '5 of Hearts' : 5, '6 of Hearts' : 6, '7 of Hearts' : 7,
            '8 of Hearts' : 8, '9 of Hearts' : 9, '10 of Hearts' : 10,
            'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
            'King of Hearts' : 10, 'Ace of Diamonds' : 11, '2 of Diamonds' : 2,
            '3 of Diamonds' : 3, '4 of Diamonds' : 4, '5 of Diamonds' : 5,
            '6 of Diamonds' : 6, '7 of Diamonds' : 7, '8 of Diamonds' : 8,
            '9 of Diamonds' : 9, '10 of Diamonds' : 10,
            'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
            'King of Diamonds' : 10, 'Ace of Clubs' : 11, '2 of Clubs' : 2,
            '3 of Clubs' : 3, '4 of Clubs' : 4, '5 of Clubs' : 5,
            '6 of Clubs' : 6, '7 of Clubs' : 7, '8 of Clubs' : 8,
            '9 of Clubs' : 9, '10 of Clubs' : 10, 'Jack of Clubs' : 10,
            'Queen of Clubs' : 10, 'King of Clubs' : 10}

        self.purg = []
        self.deck = []

    #create overall deck for blackjack, consisting of multiple standard decks
    def create_deck(self, amt):
        #amt is # of standard decks
        for count in range(amt):
            for key, value in self.cards.items():
                card = Card(key, value)
                self.purg.append(card)

        for count in range(1, self.purg_length()-1):
            item = random.randint(1, self.purg_length()-1)

            #two different methods/probabilities?
            #self.deck.insert(0, self.purg.pop(item))

            self.deck.append(self.purg.pop(item))

                
                
    #draw a card, return card drawn
    def draw(self):
        card = self.deck.pop()
        return card
            
    def purg_length(self):
        return len(self.purg)

    def deck_length(self):
        return len(self.deck)

    #function to evaluate number of cards left and reshuffle
    def reshuffle(self, amt):

        if self.deck_length() <= 50:
            print('Reshuffling Deck...')

            for item in range(1, self.deck_length()-1):
                self.deck.pop()

            self.create_deck(amt)

        else:
            pass


    def start_hands(self, pHand, dHand):
        for count in range(2):

            card = self.draw()
            pHand.cards.append(card)

            card2 = self.draw()
            dHand.cards.append(card2)
        

        pHand.has_aces()
        dHand.has_aces()
        print('-------------------------')
        print('Dealer Card:', dHand.cards[0])
        print('-------------------------')
        print()
        print('Your Hand:')
        pHand.show()
            
            


#class for hands, consisting of multiple cards
class Hand:
    def __init__(self):
        self.cards = []
        self.choice = None
        self.done = False


    def sum(self):
        total = 0
        for item in self.cards:
            total += item.get_value()
        return total


    def draw_card(self, deckObj):
        card = deckObj.draw()
        self.cards.append(card)
        print(card)

    def show(self):
        for card in self.cards:
            print(card)

    
    def has_ace(self):
        for card in self.cards:
            if card.is_ace():
                card.ace_change()
                return True
            else:
                pass

        return False

    def has_ace2(self):
        for card in self.cards:
            if card.is_ace2():
                card.ace_reverse()
                return True
            else:
                pass

    def has_ace3(self):
        for card in self.cards:
            if card.is_ace():
                return True
            else:
                pass

        return False

    def has_aces(self):
        ace1 = False
        ace2 = False

        if self.cards[0].is_ace():
            ace1 = True

        if self.cards[1].is_ace():
            ace2 = True

        if ace1 and ace2:
            self.cards[1].ace_change()

        else:
            pass

    def split(self):
        hand2 = Hand()
        hand2.cards.append(self.cards.pop())
        hand2.choice = 'p'
        return hand2

    def bust(self):
        self.done = True

    def is_done(self):
        if self.done:
            return True
        else:
            return False

           


#game loop
#cash is wallet object
def game(cash):
    HIT = 'h'
    STAND = 's'
    DOUBLE = 'd'
    SPLIT = 'p'
    SURRENDER = 'l'
    another = 'y'
    DECK_AMT = 8    #number of standard decks to use
    BLACKJACK = 1.5 #blackjack multiplier
    game_over = False   #variable to break the loop on wins/losses
    choices = ['h','s','d','p','l']
    choices2 = ['h','s','d']
    active_hands = []   #keeps non busted hands in play, use to check game over
    hands_to_remove = 0
    split_exists = False


    #initiate deck and cash
    deck = Deck()
    deck.create_deck(DECK_AMT)

    while another == 'y':
        deck.reshuffle(DECK_AMT)
        split_exists = False

        active_hands.clear()

        if cash.get_balance() <= 0:
            print('Not enough cash to continue, buy back in')
            game_over = True
            another = ''
            break
        
        while True:
            try:
                bet = float(input('Bet: '))
                break
            except ValueError:
                print('Enter a valid number!')
            
        
        while bet > cash.get_balance():
            bet = float(input('Not enough money! Enter a different bet: '))

        print()    
        playerHand = Hand()
        dealerHand = Hand()
        deck.start_hands(playerHand, dealerHand)
        active_hands.append(playerHand)
        

        print()
        print('Total:', playerHand.sum())
        print('-------------------------')

        #check for if both have blackjack
        if playerHand.sum() == 21 and dealerHand.sum() == 21:
            print()
            print('Dealer Hand:')
            dealerHand.show()
            print('Double Blackjack, Tie')
            active_hands.remove(playerHand)
            
        #check for player blackjack
        elif playerHand.sum() == 21 and dealerHand.sum() != 21:
            print('BLACKJACK!')
            print('+$', format(bet * BLACKJACK, '.2f'), sep='')
            cash.add(bet * BLACKJACK)
            print('Cash: $', format(cash.get_balance(), '.2f'), sep='')
            active_hands.remove(playerHand)

        #check for dealer blackjack
        elif playerHand.sum() != 21 and dealerHand.sum() == 21:
            print()
            print('Dealer Blackjack!')
            dealerHand.show()
            print('-$', format(bet, ',.2f'), sep='')
            cash.subtract(bet)
            print('Cash: $', format(cash.get_balance(), '.2f'), sep='')
            active_hands.remove(playerHand)

        #play game
        else:
            print()
            print('h - hit, s - stay, d - double, p - split, l - surrender',
                  end='')
            playerHand.choice = input(': ')

            while playerHand.choice not in choices:
                playerHand.choice = input('Invalid Entry, Try Again: ')

            if playerHand.choice == SURRENDER:
                print()
                print('Surrender')   
                print('-$', format(bet * .5, ',.2f'), sep='')
                cash.subtract(bet * .5)
                print('Cash: $', format(cash.get_balance(), ',.2f'), sep='')
                active_hands.clear()

            elif playerHand.choice == DOUBLE:
                bet *= 2

            elif playerHand.choice == SPLIT:
                pHand2 = playerHand.split()
                active_hands.append(pHand2)
                pHand2.has_ace2()
                split_exists = True

            else:
                pass
             
            #player sequence
            for hand in active_hands: 

                while hand.choice != STAND and not hand.is_done():
                    print()
                    print('-------------------------')
                    print('Hand:')
                    hand.show()
                    print('-------------------------')
                    print()
                    hand.draw_card(deck)


                    #check for if we went over 21 with an ace
                    if hand.sum() > 21 and hand.has_ace():
                        print('Total:', hand.sum())
                        print()

                        if hand.choice == DOUBLE:
                            hand.choice = STAND

                        elif hand.choice == SPLIT:
                            hand.choice = input('h - hit, s - stay, d - double: ')

                            while hand.choice not in choices2:
                                hand.choice = input('Invalid Entry, Try Again: ')

                        else:
                            
                            hand.choice = input('h for hit, s for stay: ')

                            while hand.choice != HIT and hand.choice != STAND:
                                hand.choice = input('Invalid Entry, Try Again: ')

                    #check for regular bust
                    elif hand.sum() > 21 and not hand.has_ace():
                        print('Total:', hand.sum())
                        print()
                        print('Bust!')
                        print('-$', format(bet, ',.2f'), sep='')
                        cash.subtract(bet)
                        print('Cash: $', format(cash.get_balance(), '.2f'),
                                sep='')
                        hand.bust()

                    
                    else:
                        print('Total:', hand.sum())
                        print()

                        if hand.choice == DOUBLE:
                            hand.choice = STAND

                        elif hand.choice == SPLIT:
                            hand.choice = input('h - hit, s - stay, d - double: ')

                            while hand.choice not in choices2:
                                hand.choice = input('Invalid Entry, Try Again: ')

                        else:
                            hand.choice = input('h for hit, s for stay: ')

                            while hand.choice != HIT and hand.choice != STAND:
                                hand.choice = input('Invalid Entry, Try Again: ')
                        

            if len(active_hands) > 0:

                if split_exists:
                    if active_hands[1].is_done():
                        active_hands.pop(1)

                else:
                    pass

                if active_hands[0].is_done():
                    active_hands.pop(0)

                else:
                    pass
            
                
            if len(active_hands) > 0:
                print()
                print('-------------------------')
                print('Dealer Hand:')
                dealerHand.show()
                print('Total:', dealerHand.sum())
                print('-------------------------')
                

            while dealerHand.sum() < 18 and len(active_hands) > 0:

                if dealerHand.sum() == 17 and not dealerHand.has_ace():
                    break

                print()
                print('Dealer Draws:')
                dealerHand.draw_card(deck)    

                #check for if dealer went over 21 with an ace
                if dealerHand.sum() > 21 and dealerHand.has_ace():
                    print('Total:', dealerHand.sum())
                    print()

                #check if dealer has soft 17
                elif dealerHand.sum() == 17 and dealerHand.has_ace3():
                    print('Total:', dealerHand.sum())
                    print()
    

                #check for bust
                elif dealerHand.sum() > 21 and not dealerHand.has_ace():
                    print('Total:', dealerHand.sum())
                    print()
                    print('Dealer Bust!')
                    dealerHand.bust()

                    for hand in active_hands: 
                        print('+$', format(bet, ',.2f'), sep='')
                        cash.add(bet)
                        print('Cash: $', format(cash.get_balance(), '.2f'),
                              sep='')
                    active_hands.clear()

                else:
                    print('Total:', dealerHand.sum())
                    print()

                
            if len(active_hands) > 0:

                for hand in active_hands:

                    #dealer wins
                    if dealerHand.sum() > hand.sum():
                        print()
                        print('Dealer wins')
                        print('-$', format(bet, ',.2f'), sep='')
                        cash.subtract(bet)
                        print('Cash: $', format(cash.get_balance(), '.2f'),
                              sep='')
                        hand.bust()
                    
                    
                    #player wins
                    elif dealerHand.sum() < hand.sum():
                        print()
                        print('You win!')
                        print('+$', format(bet, ',.2f'), sep='')
                        cash.add(bet)
                        print('Cash: $', format(cash.get_balance(), '.2f'),
                              sep='')
                        hand.bust()
                    

                    #tie
                    else:
                        print('Tie')
                        hand.bust()
                
                    

        #play again?                   
        print()
        another = input('Play again? (y) for yes, (n) for no: ')

        while another != 'y' and another != 'n':
            another = input('Invalid Entry, Try again: ')

        game_over = False



def main():
    #menu
    choice = ''
    PLAY = 1
    ADD_FUNDS = 2
    QUIT = 3
    cash = Wallet()
    
    while choice != QUIT:
        print()
        print("Welcome to Give Tony Seven Dollars")
        print('Current Cash: $', format(cash.get_balance(), ',.2f'), sep='')
        print('----------------------------------')
        print()
        print('Choose from the following options:')
        print('1. Play')
        print('2. Add Funds')
        print('3. Quit')
        choice = int(input('Enter Menu Choice: '))
        

        if choice == PLAY:
            print()
            print("Let's Play!")
            game(cash)

        elif choice == ADD_FUNDS:
            funds = float(input('Enter how much cash you are adding: '))
            cash.add(funds)

        else:
            print('Invalid Choice, Try Again.')
            

    print()
    print('Thank you for playing!')


main()


#STILL TO DO:
#changes between h17 and s17

#change bet to be specific to hand (doubling bets on split hands not working)
#stat tracking -profit, #hands played, #enter betting strat when finished

#saving our cash amount to a file for future play sessions
#NPC characters, choose how many play with you

#one day - GUI

        
