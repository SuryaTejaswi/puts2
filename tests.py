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

    def test_subtraction(self):
        response = self.app.get('/sub?A=3&B=1')
        self.assertEqual(b'2 \n', response.data)


if __name__ == '__main__':
    unittest.main()
