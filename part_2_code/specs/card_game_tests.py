import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("clubs", 1)
        self.card2 = Card("hearts", 7)
        self.game = CardGame(self.card1, self.card2)
        self.total = self.card1.value + self.card2.value

    def test_check_for_ace(self):
        self.assertEqual(True, self.game.card1.value)

    def test_highest_card(self):
        self.assertEqual(7, self.game.card2.value)

    def test_card_total(self):
        self.assertEqual(8, self.total)