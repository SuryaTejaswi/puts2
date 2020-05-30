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
        self.assertEqual(b'6.6 \n', response.data)
        response = self.app.get('/add?A=0&B=-9292')
        self.assertEqual(b'-9292.0 \n', response.data)

        # rational numbers testing
        response = self.app.get('/add?A=5/3&B=3/4')
        self.assertEqual(b'2.4167 \n', response.data)

        # when both A and B are both floats
        response = self.app.get('/add?A=5.4&B=3.4678')
        self.assertEqual(b'8.8678 \n', response.data)

        # when A is an int and B is float
        response = self.app.get('/add?A=5&B=-3.4678')
        self.assertEqual(b'1.5322 \n', response.data)

        # when A is a float and B is an int
        response = self.app.get('/add?A=-3.4678&B=5')
        self.assertEqual(b'1.5322 \n', response.data)

        # when A is a fraction and B is an int
        response = self.app.get('/add?A=3/4&B=5')
        self.assertEqual(b'5.75 \n', response.data)

        # when A is an int and B is a fraction
        response = self.app.get('/add?A=5&B=3/4')
        self.assertEqual(b'5.75 \n', response.data)

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
        self.assertEqual(b'B should be a number (includes integers, rationals, float)! \n', response.data)

        """Test for no route with post handling"""
        response = self.app.post('/')
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', response.data)

    def test_subtraction(self):
        """Tests page with /sub route, testing subtraction feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response = self.app.get("/sub?A=6&B=4")
        self.assertEqual(b'2.0\n', response.data)

        # rational numbers testing
        response = self.app.get('/sub?A=7/3&B=3/5')
        self.assertEqual(b'1.7333\n', response.data)

        # when both A and B are both floats
        response = self.app.get('/sub?A=6.2&B=3.4678')
        self.assertEqual(b'2.7322\n', response.data)

        # when A is an int and B is float
        response = self.app.get('/sub?A=4&B=-2.4678')
        self.assertEqual(b'6.4678\n', response.data)

        # when A is a float and B is an int
        response = self.app.get('/sub?A=-2.4678&B=6')
        self.assertEqual(b'-8.4678\n', response.data)

        # when A is a fraction and B is an int
        response = self.app.get('/sub?A=5/4&B=2')
        self.assertEqual(b'-0.75\n', response.data)

        # when A is an int and B is a fraction
        response = self.app.get('/sub?A=5&B=3/4')
        self.assertEqual(b'4.25\n', response.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response = self.app.get('/sub?A=-6/0&B=3/5')
        self.assertEqual(b"A's denominator shouldn't be 0! \n", response.data)

        # when B = x/0 where x belongs to any integer
        response = self.app.get('/sub?A=-2&B=2/0')
        self.assertEqual(b"B's denominator shouldn't be 0! \n", response.data)

        # when A is a non-number type
        response = self.app.get('/sub?A=x&B=langa')
        self.assertEqual(b"A should be a number (includes integers, rationals, float)! \n", response.data)

        # when B is a non-number type
        response = self.app.get('/sub?4=1&B=i')
        self.assertEqual(b"B should be a number (includes integers, rationals, float)! \n", response.data)

        # Handling of POST Method
        response = self.app.post('/sub', data=dict(A='1', B='2'))
        self.assertEqual(b'1.0\n', response.data)

    def test_multiplication(self):
        """Tests page with /mul route, testing multiplication feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response = self.app.get('/mul?A=5&B=4')
        self.assertEqual(b'20.0\n', response.data)

        # rational numbers testing
        response = self.app.get('/mul?A=4/3&B=5/4')
        self.assertEqual(b'1.6667\n', response.data)

        # when both A and B are both floats
        response = self.app.get('/mul?A=2.6&B=5.7894')
        self.assertEqual(b'15.0524\n', response.data)

        # when A is an int and B is float
        response = self.app.get('/mul?A=5&B=-3.4678')
        self.assertEqual(b'-17.339\n', response.data)

        # when A is a float and B is an int
        response = self.app.get('/mul?A=-2.4567&B=5')
        self.assertEqual(b'-12.2835\n', response.data)

        # when A is a fraction and B is an int
        response = self.app.get('/mul?A=5/4&B=2')
        self.assertEqual(b'2.5\n', response.data)

        # when A is an int and B is a fraction
        response = self.app.get('/mul?A=5&B=3/4')
        self.assertEqual(b'3.75\n', response.data)

        # corner cases testing
        # when A = x/0 where x belongs to any integer
        response = self.app.get('/mul?A=-5/0&B=3/4')
        self.assertEqual(b"A's denominator shouldn't be 0! \n", response.data)

        # when B = x/0 where x belongs to any integer
        response = self.app.get('/mul?A=-2&B=4/0')
        self.assertEqual(b"B's denominator shouldn't be 0! \n", response.data)

        # when A is a non-number type
        response = self.app.get('/mul?A=x&B=zingo')
        self.assertEqual(b"A should be a number (includes integers, rationals, float)! \n", response.data)

        # when B is a non-number type
        response = self.app.get('/mul?A=1&B=y')
        self.assertEqual(b"B should be a number (includes integers, rationals, float)! \n", response.data)

        # Handling of POST method
        response = self.app.post('/mul', data=dict(A='1', B='y'))
        self.assertEqual(b'B should be a number (includes integers, rationals, float)! \n', response.data)

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
        self.assertEqual(b"A should be a number (includes integers, rationals, float)! \n", response.data)

        # when B is a non-number type
        response = self.app.get('/div?A=1&B=s')
        self.assertEqual(b"B should be a number (includes integers, rationals, float)! \n", response.data)

        # Extra case when B is zero
        response = self.app.get('/div?A=1&B=0')
        self.assertEqual(b"B's value shouldn't be zero! \n", response.data)

        # Handling of POST Method
        response = self.app.post('/div', data=dict(A='1', B='0'))
        self.assertEqual(b"B's value shouldn't be zero! \n", response.data)


if __name__ == '__main__':
    unittest.main()
