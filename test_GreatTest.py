import unittest
import GreatTest


class testGreatTest(unittest.TestCase):
    def test_adding(self):
        self.assertEqual(GreatTest.add(1, 2), 3)
