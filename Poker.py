import random

VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '1':10, 'J':11, 'Q':12, 'K':13, 'A':14}
SUITS = {'c':1, 'd':2, 'h':3, 's':4}
class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit
    self.valueRank = VALUES[value]
    self.suitRank = SUITS[suit]

  def compare(self, card):
    if self.valueRank>card.valueRank:
        return self
    elif self.valueRank<card.valueRank:
        return card
    else:
        if self.suitRank>card.suitRank:
            return self
        elif self.suitRank<card.suitRank:
            return card
        else:
            return "SAME"

  def __str__(self):
    return (self.value+", "+ self.suit)

class Deck:
    def __init__(self):
        self.cards=[]
        for suit in SUITS.keys():
            for rank in VALUES.keys():
                self.cards.append(Card(rank,suit))
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        retstr = ""
        for card in self.cards:
            retstr += str(card)
            retstr += "\n"
        return retstr

    def pop(self, amount):
        cardlist=[]
        for i in range(amount):
            cardlist.append(self.cards.pop(0))
        return cardlist

class Hand:
    def __init__(self,deck,size=2):
        self.cards = deck.pop(size)
    def __str__(self):
        retstr=""
        for card in self.cards:
            retstr += str(card)
            retstr += "\n"
        return retstr

class Game:
    def __init__(self,minimum_bet,maximum_bet):
        self.players = {}
        self.deck = Deck()
        self.pot = 0
        self.minimum_bet = minimum_bet
        self.maximum_bet = maximum_bet

    def payout(self,player):
        player.money+=self.pot
        self.pot = 0

    def newRound(self):
        self.deck = Deck()
        self.pot = 0

class Player:
    def __init__(self,name,buyin):
        self.name = name
        self.money=buyin

    def lose(self,game):
        print("Player {} loses".format(self.name))
        del game.players[self.name]

    def bet(self,game,amount):
        if self.money>=amount:
            game.pot += amount
            self.money-=amount
        else:
            print("Player {} has not enough money".format(self.name))
