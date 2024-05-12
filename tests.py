import unittest
from checkout import *
class TestCheckout(unittest.TestCase):
    def test_total_price(self):
        assert price("") == 0
        assert price("A") == 50
        assert price("AB") == 80
        assert price("CDBA") == 115
        assert price("AA") == 100
        assert price("AAA") == 130
        assert price("AAAA") == 180
        assert price("AAAAA") == 230
        assert price("AAAAAA") == 260
        assert price("AAAB") == 160
        assert price("AAABB") == 175
        assert price("AAABBD") == 190
        assert price("DABABA") == 190

