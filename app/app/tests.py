"""
Creating TDD
"""
from django.test import SimpleTestCase
from app import calc

class CalcuTest(SimpleTestCase):
    def test_minus(self):
        res = calc.minus(7,2)
        self.assertEqual(res,5)