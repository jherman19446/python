"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    round_number = [number]
    round_number.append(number + 1)
    round_number.append(number + 2)
    return round_number




def concatenate_rounds(rounds_1, rounds_2):
    rounds1, rounds2 = rounds_1, rounds_2
    return rounds1 + rounds2




def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False
 


def card_average(hand):
    number_of_cards = len(hand)
    average = sum(hand) / (number_of_cards)
    return average 
 


def approx_average_is_average(hand):
    from statistics import median
    end_averages = (hand[0] + hand[-1]) / 2
    median_card = median(hand)
    real_average = card_average(hand)
    if end_averages == real_average or median_card == real_average:
        return True
    return False
    


def average_even_is_average_odd(hand):
    even = hand[0::2]
    odd = hand[1::2]
    average_even = sum(even) / len(even)
    average_odd = sum(odd) / len(odd)
    if average_even == average_odd:
        return True
    return False
   


def maybe_double_last(hand):
    new_hand = [22]
    if hand[-1] == 11:
        return hand[:-1] + new_hand
    return hand


