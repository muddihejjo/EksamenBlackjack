#Run - python -m unittest test_BlackJack.py
from BlackjackEksamen import Kort
from unittest import TestCase
from BlackjackEksamen import *

class testSpil(TestCase):

    def test_SpilIgen(self):

        self.assertIsInstance(igangværendeSpil, bool)


class test_Resultat(TestCase):  

    def test_Tab(self):
        penge = Penge()
        penge.total = 100
        penge.indsæt = 10
        penge.taberBet()
        self.assertEqual(penge.total, 90)    
    
    def test_Vin(self):
        penge = Penge()
        penge.total = 100
        penge.indsæt = 10
        penge.vinderBet()
        self.assertEqual(penge.total, 110)

class TestKort(TestCase):
    def Ace_duplikat(self):
        hånd = Hånd()
        hånd.tilføjKort(Kort("Spades", "Ace"))
        hånd.tilføjKort(Kort("Diamonds", "Ace"))
        hånd.justerAce()
        værdi = hånd.værdi
        self.assertEqual(værdi,12)

        


if __name__ == "__main__":
    unittest.main()

