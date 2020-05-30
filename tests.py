import unittest
import main


class OnlineCalculatorTestCase(unittest.TestCase):
    """Test features of online calculator"""

    def setUp(self):
        """Setup """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_division(self):
        """ Testing division feature of the calculatore"""
        # printing integral value correctly
        response = self.app.get('/div?A=6&B=3')
        self.assertEqual(b'2.0\n', response.data)

        # integer numbers testing
        response = self.app.get('/div?A=7&B=3')
        self.assertEqual(b'2.3333\n', response.data)

        # rational numbers testing
        response = self.app.get('/div?A=4/3&B=3/4')
        self.assertEqual(b'1.7778\n', response.data)

        # when both A and B are both floats
        response = self.app.get('/div?A=2.4&B=4.7788')
        self.assertEqual(b'0.5022\n', response.data)

        # when A is an int and B is float
        response = self.app.get('/div?A=3&B=-5.2142')
        self.assertEqual(b'-0.5754\n', response.data)

        # when A is a float and B is an int
        response = self.app.get('/div?A=2.1365&B=5')
        self.assertEqual(b'0.4273\n', response.data)

        # when A is a fraction and B is an int
        response = self.app.get('/div?A=3/4&B=5')
        self.assertEqual(b'0.15\n', response.data)

        # when A is an int and B is a fraction
        response = self.app.get('/div?A=5&B=3/4')
        self.assertEqual(b'6.6667\n', response.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response = self.app.get('/div?A=-5/0&B=3/4')
        self.assertEqual(b"A's denominator shouldn't be 0! \n", response.data)

        # when B = x/0 where x belongs to any integer
        response = self.app.get('/div?A=-2&B=4/0')
        self.assertEqual(b"B's denominator shouldn't be 0! \n", response.data)

        # when A is a non-number type
        response = self.app.get('/div?A=x&B=auckaa')
        self.assertEqual(b"A should be number(includes integers, rationals, float)! \n", response.data)

        # when B is a non-number type
        response = self.app.get('/div?A=1&B=s')
        self.assertEqual(b"B should be number(includes integers, rationals, float)! \n",
                         response.data)

        # Extra case when B is zero
        response = self.app.get('/div?A=1&B=0')
        self.assertEqual(b"B's value shouldn't be zero! \n", response.data)

        # Handling of POST Method
        response = self.app.post('/div', data=dict(A='1', B='0'))
        self.assertEqual(b"B's value shouldn't be zero! \n", response.data)


if __name__ == '__main__':
        unittest.main()
