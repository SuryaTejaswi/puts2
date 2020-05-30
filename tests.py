import unittest
import main


class OnlineCalculatorTestCase(unittest.TestCase):
    """Test features of online calculator"""

    def setUp(self):
        """Setup """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_subtraction(self):
        """Tests page with /sub route, testing subtraction feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get("/sub?A=6&B=4")
        self.assertEqual(b'2.0\n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/sub?A=7/3&B=3/5')
        self.assertEqual(b'1.7333\n', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/sub?A=6.2&B=3.4678')
        self.assertEqual(b'2.7322\n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/sub?A=4&B=-2.4678')
        self.assertEqual(b'6.4678\n', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/sub?A=-2.4678&B=6')
        self.assertEqual(b'-8.4678\n', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/sub?A=5/4&B=2')
        self.assertEqual(b'-0.75\n', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/sub?A=5&B=3/4')
        self.assertEqual(b'4.25\n', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response_data = self.app.get('/sub?A=-6/0&B=3/5')
        self.assertEqual(b"A's denominator shouldn't be 0! \n", response_data.data)

        # when B = x/0 where x belongs to any integer
        response_data = self.app.get('/sub?A=-2&B=2/0')
        self.assertEqual(b"B's denominator shouldn't be 0! \n", response_data.data)

        # when A is a non-number type
        response_data = self.app.get('/sub?A=x&B=langa')
        self.assertEqual(b"A should be number(includes integers, rationals, float)! \n", response_data.data)

        # when B is a non-number type
        response_data = self.app.get('/sub?4=1&B=i')
        self.assertEqual(b"B should be number(includes integers, rationals, float)! \n", response_data.data)

        # Handling of POST Method
        response_data = self.app.post('/sub', data=dict(A='1', B='2'))
        self.assertEqual(b'1.0\n', response_data.data)


if __name__ == '__main__':
    unittest.main()
