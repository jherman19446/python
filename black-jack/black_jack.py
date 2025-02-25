"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card):
    if (card in 'JQK'):
        return 10
    if (card == 'A'):
        return 1
    return int(card)
   

    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """



def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one,card_two

    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """



def value_of_ace(card_one, card_two):
    card1 = value_of_card(card_one)
    card2 = value_of_card(card_two)
    if card1 == 1 and card1 + card2 <= 10: return 1
    if card2 == 1 and card1 + card2 <= 10: return 1
    if card1 == 1 and card1 + card2 > 11: return 11
    if card2 == 1 and card1 + card2 > 11: return 11
    if card1 + card2 <= 10: return 11
    else: return 1
    


    
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """



def is_blackjack(card_one, card_two):
    face_card = {'10','J', 'Q', 'K'}
    high_ace = {'A'}
    if card_one in face_card and card_two in high_ace: return True
    if card_two in face_card and card_one in high_ace: return True
    else: return False
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """


def can_split_pairs(card_one, card_two):
    face_card = ['10','J','Q','K']
    if card_one in face_card and card_two in face_card:
        return True
    if card_one == card_two:
        return True
    else: 
        return False
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """



def can_double_down(card_one, card_two):
    value = value_of_card(card_one) + value_of_card(card_two)
    print(value)
    if value_of_card(card_one) == 1 and value_of_card(card_two) == 1:
        return False
    if value_of_card(card_one) == 1 or value_of_card(card_two) == 1 and value <= 11 >= 9:
        return True
    if value_of_card(card_one) == 10 or value_of_card(card_two) == 10:
            return False
    if value <= 11 >= 9:
        return True
    return False
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """


