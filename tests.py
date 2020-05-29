import unittest
import main


class OnlineCalculatorTestCase(unittest.TestCase):
    """Test features of online calculator"""

    def setUp(self):
        """Setup """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_multiplication(self):
        """Test for multiplication resource"""
        response = self.app.get('/mul?A=5&B=4')
        self.assertEqual(b'20 \n', response.data)
        response_data = self.app.get('/mul?A=5/3&B=3/4')
        self.assertEqual(b'1.250 \n', response_data.data)
        response_data = self.app.get('/mul?A=5.4&B=3.4678')
        self.assertEqual(b'18.726 \n', response_data.data)
        response_data = self.app.get('/mul?A=3/4&B=5')
        self.assertEqual(b'3.750 \n', response_data.data)


if __name__ == '__main__':
    unittest.main()
