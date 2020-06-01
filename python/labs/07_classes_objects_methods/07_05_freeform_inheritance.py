'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.


Created on Thu May 28 17:12:31 2020

@author: alex_me

Encoding:

    Suite:
    Spades	    ↦  3
    Hearts	    ↦  2
    Diamonds	↦  1
    Clubs	    ↦  0

    Rank:
    Ace     ↦   1
    Nums    ↦   2-10
    Jack	↦	11
    Queen	↦	12
    King	↦	13

'''
import random


class Card:
    """Constructor for cards.
       Standard card is Ace of Clubs"""

    suit_names = ("Clubs", "Diamonds", "Hearts", "Spades")
    card_ranks = ("None", "Ace", "2", "3", "4", "5", "6", "7", "8",
                  "9", "10", "Jack", "Queen", "King")

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Print decoded card rank|suit."""
        return f"{Card.card_ranks[self.rank]} of {Card.suit_names[self.suit]}"

    def __lt__(self, other):
        """Compare cards: suits first then card ranks"""
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """Constructor for decks."""

    def __init__(self):
        """Generate base deck of 52 cards."""
        self.cards = []
        for s in range(4):
            for r in range(1, 14):
                card = Card(s, r)  # Call for Cards class to create card
                self.cards.append(card)

    def __str__(self):
        """Generate list of all cards in the deck."""
        d_list = []
        for n_card in self.cards:
            d_list.append(str(n_card))
        return "\n".join(d_list)

    def pop_card(self):
        """Take card from deck"""
        return self.cards.pop()

    def add_card(self, card):
        """Add card to deck"""
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        """Move number of cards to hand."""
        for n in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hands, num_cards_hand):
        """Generate number of hands with number of cards."""
        hands_list = []
        for n_han in range(num_hands):
            hand_elem = Hand(f"Hand N{n_han + 1}")
            self.move_cards(hand_elem, num_cards_hand)
            hands_list.append(hand_elem)
        return hands_list


class Hand(Deck):
    """Hand is child class of Deck. Here we store cards for one hand."""

    def __init__(self, label=""):
        self.cards = []
        self.label = label


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_keys_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """

        self.suits = {}
        self.ranks = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a five cards of the same suit,
        False otherwise. Works correctly for hands with more than 5 cards.
        """

        self.suit_keys_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has a two cards of the same rank,
        False otherwise. Works correctly for more than 1 card.
        """

        self.suit_keys_hist()
        for val_p in self.ranks.values():
            if val_p == 2:
                return True
        return False

    def has_two_pairs(self):
        """Returns True if the hand has a two cards of the same rank and
        two cards of another rank. False otherwise.
        Works correctly for hands with 4 or more cards.
        """

        self.suit_keys_hist()
        count_tp = []
        for val_tp in self.ranks.values():
            if val_tp == 2:
                count_tp.append(val_tp)
        if len(count_tp) >= 2:
            return True
        return False

    def three_of_a_kind(self):
        """Returns True if the hand has a three cards of the same rank,
        False otherwise. Works correctly for hands with 3 or more cards.
        """

        self.suit_keys_hist()
        for val_top in self.ranks.values():
            if val_top == 3:
                return True
        return False

    def four_of_a_kind(self):
        """Returns True if the hand has a four cards of the same rank,
        False otherwise. Works correctly for hands with 4 or more cards.
        """

        self.suit_keys_hist()
        for val_f in self.ranks.values():
            if val_f == 4:
                return True
        return False

    def has_full_house(self):
        """Returns True if the hand has a three cards of the same rank and
        two cards of another rank. False otherwise.
        Works correctly for hands with 5 or more cards.
        """

        self.suit_keys_hist()
        count_fh = []
        for val_fh in self.ranks.values():
            if val_fh == 3 and 3 not in count_fh:
                count_fh.append(val_fh)
            if val_fh == 2 and 2 not in count_fh:
                count_fh.append(val_fh)
        if len(count_fh) == 2:
            return True
        return False

    def has_straight(self):
        """Returns True if the hand has a five cards of rank sequence and
        False otherwise. Works correctly for hands with 5 or more cards.
        """

        self.suit_keys_hist()
        lst = list(self.ranks.keys())
        lst.sort()
        run = []
        result = [run]
        expect = None
        for v in lst:
            if (v == expect) or (expect is None):
                run.append(v)
            else:
                run = [v]
                result.append(run)
            expect = v + 1
        for res in result:
            if len(res) >= 5:
                return True
            return False

    def has_straight_flush(self):
        """Returns True if the hand has a five cards of rank sequence and one
        suit, False otherwise. Works correctly for hands with 5 or more cards.
        """

        self.suit_keys_hist()
        lst = list(self.ranks.keys())
        lst.sort()
        for val in self.suits.values():
            if val >= 5:
                run = []
                result = [run]
                expect = None
                for v in lst:
                    if (v == expect) or (expect is None):
                        run.append(v)
                    else:
                        run = [v]
                        result.append(run)
                    expect = v + 1
                for res in result:
                    if len(res) >= 5:
                        return True
                    return False
            return False

    def classify(self):
        """Classification of card combinations power."""

        max_comb = []
        dict_comb = {"Pair": 0, "Two Pairs": 1, "Three of a kind": 2,
                     "Straight": 3, "Flush": 4, "Full House": 5,
                     "Four of a kind": 6, "Straight Flush": 7}
        for v_line in dict_comb.values():
            if (self.has_pair() is True) and (self.has_two_pairs()) is False:
                max_comb.append(0)
            elif (self.has_pair() is True) and (self.has_two_pairs() is True):
                max_comb.append(1)
            elif self.three_of_a_kind() is True:
                max_comb.append(2)
            elif self.has_straight() is True:
                max_comb.append(3)
            elif self.has_flush() is True:
                max_comb.append(4)
            elif self.has_full_house() is True:
                max_comb.append(5)
            elif self.four_of_a_kind() is True:
                max_comb.append(6)
            elif self.has_straight_flush() is True:
                max_comb.append(7)
            else:
                return "No combination"
        max_comb.sort()
        what_comb_best = list(dict_comb.keys())[list(dict_comb.values()
                                                     ).index(max_comb[-1])]
        return what_comb_best


def run_one_round(n_range, n_cards):
    """Take two arguments and return some hands withs number of cards
       and max winning combination.

    Input:
        n_range (int): how many hands to print.
        n_cards (int): how many cards must be in one hand.

    Return:
        print: n_range hands with n_cards per hand printed.

    """
    for i in range(n_range):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, n_cards)
        hand.sort()
        print(hand)
        print("Highest combination:", hand.classify())
        print('')


def run_multiple_rounds(n_trials, n_cardz):
    """Gather statistic for combinations in n-trials with run_one_round
    function.

    Input:
        n_trials (int): number of trials.
        n_cardz (int): number of cardt per hand.

    Return:
        dict: frequency for each combination based on number of trials.

    """
    comb_counts = {}
    for t in range(n_trials):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, n_cardz)
        if hand.classify() in comb_counts:
            comb_counts[hand.classify()] += 1
        else:
            comb_counts[hand.classify()] = 1

    for k, v in comb_counts.items():
        comb_counts[k] = round((v / n_trials) * 100, 2)

    comb_counts = {k: v for k, v in sorted(comb_counts.items(),
                                           key=lambda x: x[1],
                                           reverse=True)}
    return print(comb_counts)


def find_defining_class(obj, method_name):
    """This function will show the class that provodes the method,
       for example: find_defining_class(hand, 'shuffle')"""
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty


if __name__ == '__main__':
    # deal the cards and classify the hands
    run_one_round(1, 7)
    print("\n")
    run_multiple_rounds(50000, 7)
