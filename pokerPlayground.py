import Poker

if __name__ == '__main__':
    # a = Card.Card('J','d')
    # b = Card.Card('Q','c')
    # print(a.compare(b))
    deck = Poker.Deck()
    print(Poker.Hand(deck,2))