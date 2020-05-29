import unittest
import main


class OnlineCalculatorTestCase(unittest.TestCase):
    """Test features of online calculator"""

    def setUp(self):
        """Setup """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_subtraction(self):
        response = self.app.get('/sub?A=3&B=1')
        self.assertEqual(b'2 \n', response.data)
        response = self.app.get('/sub?A=5&B=-100')
        self.assertEqual(b'105 \n', response.data)
        response = self.app.get('/sub?A=10&B=-10')
        self.assertEqual(b'20 \n', response.data)


if __name__ == '__main__':
    unittest.main()
