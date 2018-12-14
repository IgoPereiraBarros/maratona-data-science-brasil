from random import choice, sample, shuffle
import unittest

class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		self.seq = list(range(10))

	def test_shuffle(self):
		shuffle(self.seq)
		self.seq.sort()
		self.assertEqual(self.seq, list(range(10)))

		self.assertRaises(TypeError, shuffle, (1,2,3))

	def test_choice(self):
		element = choice(self.seq)
		self.assertTrue(element in self.seq)

	def test_sample(self):
		with self.assertRaises(ValueError):
			sample(self.seq, 20)
		for element in sample(self.seq, 5):
			self.assertTrue(element in self.seq)

if __name__ == '__main__':
	unittest.main()
