# 7.1
class Card(object):
    """ abstract data type for card object """
    def __init__(self, suit, value)
        # probably want to ensure that values are allowed
        if suit not in ["spade", "heart", "club", "diamond"]:
            raise
        self.suit = suit
        self.value = value

class DeckOfCards(object):
    def __init__(self):
        """ initializes a list of 52 cards in the deck """
        # e.g., self.deck = [Card("Space", "1"), Card()]

    def shuffle(self):
        """ shuffle cards """

    def pop(self):
        #remove the top card
        return self.deck.pop()

    def peek(self):
        """ view the top card in the deck but don't remove """


class CardGame(object):
    def __init__(self):
        """ initializes the 52 cards in the deck """
        # e.g., self.deck = [Card("Space", "1"), Card()]

    def shuffle(self):
        """ shuffle cards """

class Poker(CardGame):
    """ poker game
    methods could include:
        draw
        fold
        initialize_opponents
    """

class Blackjack(CardGame):
    """
    methods could include:
        hit

    """

# 7.4
class PlayerBase(object):
    """ abstract base class for a player, used by both human and computer controlled players """
    def get_turn(self):
        """ """

class ComputerPlayer(PlayerBase):
    def set_difficulty(self):
        """
        :return:
        """

class ChessPiece(object):
    """ abstract class for chess piece"""


class King(ChessPiece):

class ChessPiecePosition(object):
    """ """