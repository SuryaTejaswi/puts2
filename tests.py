import unittest
import main


class OnlineCalculatorTestCase(unittest.TestCase):
    """Test features of online calculator"""

    def setUp(self):
        """Setup """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_no_resources(self):
        """Test for no route"""
        response = self.app.get('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', response.data)

    def test_division(self):
        """Test for division"""
        response = self.app.get('/div?A=6&B=3')
        self.assertEqual(b'2 \n', response.data)


if __name__ == '__main__':
    unittest.main()
