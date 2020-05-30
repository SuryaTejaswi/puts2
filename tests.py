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
        self.assertEqual(b'8.0 \n', response.data)
        response = self.app.get('/add?A=6&B=3/5')
        self.assertEqual(b'6.6000 \n', response.data)
        response = self.app.get('/add?A=0&B=-9292')
        self.assertEqual(b'-9292.0 \n', response.data)
        # integer numbers testing
        response = self.app.get('/add?A=5&B=3')
        self.assertEqual(b'8 \n', response.data)

        # rational numbers testing
        response = self.app.get('/add?A=5/3&B=3/4')
        self.assertEqual(b'2.417 \n', response.data)

        # when both A and B are both floats
        response = self.app.get('/add?A=5.4&B=3.4678')
        self.assertEqual(b'8.868 \n', response.data)

        # when A is an int and B is float
        response = self.app.get('/add?A=5&B=-3.4678')
        self.assertEqual(b'1.532 \n', response.data)

        # when A is a float and B is an int
        response = self.app.get('/add?A=-3.4678&B=5')
        self.assertEqual(b'1.532 \n', response.data)

        # when A is a fraction and B is an int
        response = self.app.get('/add?A=3/4&B=5')
        self.assertEqual(b'5.750 \n', response.data)

        # when A is an int and B is a fraction
        response = self.app.get('/add?A=5&B=3/4')
        self.assertEqual(b'5.750 \n', response.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response = self.app.get('/add?A=-5/0&B=3/4')
        self.assertEqual(b"A's denominator shouldn't be 0! \n", response.data)

        # when B = x/0 where x belongs to any integer
        response = self.app.get('/add?A=-2&B=4/0')
        self.assertEqual(b"B's denominator shouldn't be 0! \n", response.data)

        # when A is a non-number type
        response = self.app.get('/add?A=x&B=zingo')
        self.assertEqual(b"A should be a number (includes integers, rationals, float)! \n", response.data)

        # when B is a non-number type
        response = self.app.get('/add?A=1&B=y')
        self.assertEqual(b"B should be a number (includes integers, rationals, float)! \n", response.data)

        # Handling of POST Method 
        response = self.app.post('/add?A=1&B=2)')
        self.assertEqual(b"3 \n", response.data)


if __name__ == '__main__':
    unittest.main()
