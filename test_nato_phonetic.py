import unittest
from nato_phonetic import frequency_counter, spell_word # type: ignore

class TestNatoPhonetic(unittest.TestCase):

    def test_frequency_counter(self):
        self.assertEqual(frequency_counter([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})
        self.assertEqual(frequency_counter(['a', 'b', 'a']), {'a': 2, 'b': 1})
        self.assertEqual(frequency_counter([]), {})

    def test_spell_word(self):
        self.assertEqual(spell_word('Drake'), ['Delta', 'Romeo', 'Alpha', 'Kilo', 'Echo'])
        self.assertEqual(spell_word('College'), ['Charlie', 'Oscar', 'Lima', 'Lima', 'Echo', 'Golf', 'Echo'])
        self.assertEqual(spell_word('McHenry'), ['Mike', 'Charlie', 'Hotel', 'Echo', 'November', 'Romeo', 'Yankee'])
        self.assertEqual(spell_word('Amazon'), ['Alpha', 'Mike', 'Alpha', 'Zulu', 'Oscar', 'November'])

if __name__ == '__main__':
    # Create a test suite and add the test cases
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNatoPhonetic)
    
    # Run the test suite and show the results
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)