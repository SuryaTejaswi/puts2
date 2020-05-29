import unittest
import main


class OnlineCalculatorTestCase(unittest.TestCase):
    """Test features of online calculator"""

    def setUp(self):
        """Setup """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_addition(self):
        """Test for addition resource"""
        response = self.app.get('/add?A=5&B=3')
        self.assertEqual(b'8 \n', response.data)
        response = self.app.get('/add?A=6&B=3/5')
        self.assertEqual(b'6.600 \n', response.data)
        response = self.app.get('/add?A=0&B=-9292')
        self.assertEqual(b'-9292 \n', response.data)


if __name__ == '__main__':
    unittest.main()
