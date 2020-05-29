import unittest
import main


class OnlineCalculatorTestCase(unittest.TestCase):
    """Test features of online calculator"""

    def setUp(self):
        """Setup """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_division(self):
        """Test for division"""
        response = self.app.get('/div?A=6&B=3')
        self.assertEqual(b'2 \n', response.data)
        response = self.app.get('/div?A=5&B=3')
        self.assertEqual(b'1.667 \n', response.data)
        response = self.app.get('/div?A=5/3&B=3/4')
        self.assertEqual(b'2.222 \n', response.data)
        response = self.app.get('/div?A=5.4&B=3.4678')
        self.assertEqual(b'1.557 \n', response.data)


if __name__ == '__main__':
    unittest.main()
