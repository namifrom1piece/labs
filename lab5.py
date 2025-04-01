#############################
# APS106 Winter 2025 - lab5 #
# Card Game                 #
#############################
# Extract information from lists and nested lists using indexing
# Add and remove elements from lists
# Understand aliasing by modifying lists passed to functions as parameters
# Utilize loops to iterate through lists
# Practice writing and debugging boolean expressions, conditionals, and loop

import random

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - DO NOT EDIT
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    cards = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            cards.append([suit,number])

    return cards


def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck


######################
# Part 1 - Deal Card #
######################

def deal_card(hand, deck):
    """
    (list,list) -> None

    Deals a card from the first element in the deck list and add it to the list
    representing the player's hand. This function should remove the first card
    from the deck list and append it to hand list.

    Parameters
    ----------
    hand : list
        List representing the player's hand
    deck : list
        List representing the deck of cards
    """
    # To Do: Complete the function
    hand.append(deck.pop(0))




########################
# Part 2 - Score Cards #
########################

def score_cards(hand):
    """
    (list) -> int

    Calculate the score of the player's hand. The score is the sum of the values
    of the cards in the hand. Number cards are worth their number value, face cards (jack, queen, king)
    are worth 10, and aces are worth 11. If the hand contains an ace and the score
    is greater than 21, the ace should be worth 1 instead of 11.

    Parameters
    ----------
    hand : list
        List representing the player's hand

    Returns
    -------
    int
        The score of the collection of cards in the hand
    """
    # To Do: Complete the function
    score = 0
    ace_count = 0
    for card in hand:
        value = card[1]
        if value > 10:
            score += 10
        elif value == 1:
            score += 11
            ace_count += 1
        else:
            score += value
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score

######################
# Part 3 - Play Game #
######################

def play(shuffled_deck):
    """
    (list) -> [str,int,int]

    Play the card game of with the shuffled deck of cards.

    Parameters
    ----------
    shuffled_deck : list
        List representing the shuffled deck of cards

    Returns
    -------
    list
        A list containing the winner of the game, the dealer's score, and the player's score.
        The winner is a string representing the winner of the game ('player' or 'dealer').
        The dealer's score is an integer representing the score of the player's hand.
        The player's score is an integer representing the score of the dealer's hand.
    """

    # define the player and dealer hands
    player_hand = []
    dealer_hand = []

    # To Do: Complete the function
    deal_card(player_hand, shuffled_deck)
    deal_card(dealer_hand, shuffled_deck)
    deal_card(player_hand, shuffled_deck)
    deal_card(dealer_hand, shuffled_deck)

    player_score = score_cards(player_hand)
    dealer_score = score_cards(dealer_hand)

    while player_score < 14:
        deal_card(player_hand, shuffled_deck)
        player_score = score_cards(player_hand)
    
    if player_score > 21:
        return ['dealer', dealer_score, player_score]
    
    while dealer_score < player_score:
        deal_card(dealer_hand, shuffled_deck)
        dealer_score = score_cards(dealer_hand)

    if dealer_score > 21:
        return ['player', dealer_score, player_score]

    elif player_score > dealer_score:
        return ['player', dealer_score, player_score]

    else:
        return ['dealer', dealer_score, player_score]        


deck = [['hearts', 5], ['spades', 11], ['clubs', 1], ['diamonds', 2], ['clubs', 3], ['hearts', 4], ['spades', 6], ['diamonds', 3], ['hearts', 11], ['spades', 6], ['diamonds', 9]]
print('deck:', deck[:10])
print('result: ', play(deck))