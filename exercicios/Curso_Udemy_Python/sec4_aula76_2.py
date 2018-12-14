class TestExemple:

	def test_one(self):
		linguagem = 'python'
		assert linguagem[0::2] == 'pto'
		
	def test_two(self):
		assert 10 == 10