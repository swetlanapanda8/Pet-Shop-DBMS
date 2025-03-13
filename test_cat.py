import unittest
from unittest.mock import patch
from Cat import Cat

class TestCat(unittest.TestCase):
    @patch('random.randint', return_value=7)
    def test_initial_age(self, mock_randint):
        cat = Cat()
        self.assertGreaterEqual(cat.get_age(), 5)
        self.assertLessEqual(cat.get_age(), 10)
        self.assertEqual(cat.get_age(), 7)

    def test_initial_age_random(self):
        cat = Cat()
        self.assertGreaterEqual(cat.get_age(), 5)
        self.assertLessEqual(cat.get_age(), 10)

    def test_speak_default(self):
        cat = Cat()
        with patch('builtins.print') as mocked_print:
            cat.speak()
            mocked_print.assert_called_once_with("meow")

    def test_speak_custom(self):
        cat = Cat()
        with patch('builtins.print') as mocked_print:
            cat.speak("hiss")
            mocked_print.assert_called_once_with("hiss")

    def test_set_name(self):
        cat = Cat()
        cat.set_name("Garfield")
        self.assertEqual(cat.get_name(), "Garfield")
        cat.set_name("Tom")
        self.assertEqual(cat.get_name(), "Tom")
        self.assertListEqual(cat.get_names(), [None, "Garfield", "Tom"])

    def test_get_average_name_length(self):
        cat = Cat("Whiskers")
        cat.set_name("Garfield")
        cat.set_name("Tom")
        self.assertAlmostEqual(cat.get_average_name_length(), (len("Whiskers") + len("Garfield") + len("Tom")) / 3)

    def test_speak_increments_age(self):
        cat = Cat()
        initial_age = cat.get_age()
        for _ in range(5):
            cat.speak()
        self.assertEqual(cat.get_age(), initial_age + 1)

if __name__ == '__main__':
    unittest.main()
