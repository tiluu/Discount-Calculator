import unittest
from discount_calc import DiscountCalculator


class DiscountCalculatorTests(unittest.TestCase):
	def test_ten_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100,10,'percent')
		self.assertEqual(10.0, result)
	def test_fifteen_percent_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(100, 15, 'percent')
		self.assertEqual(15.0,result)
	
	def test_five_dollar_discount(self):
		discount_calculator = DiscountCalculator()
		result = discount_calculator.calculate(200, 5, 'absolute')
		self.assertEqual(5, result)
	
	def test_invalid_discount(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises(ValueError, discount_calculator.calculate, 250, 5, 'random')

	def test_excess_discount(self):
		discount_calculator = DiscountCalculator()
		self.assertRaises(ValueError, discount_calculator.calculate, 250, 110, 'percent')
	