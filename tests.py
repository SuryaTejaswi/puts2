import unittest
import main


class AdvanceCalc(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testEmpty_Page(self):
        # Test the page with an empty route
        respond = self.app.get("/")
        self.assertEqual(b'Usage: <operation>?<X1, X2, X3, ..., XN>\n', respond.data)

    def testing_avg(self):
        respond = self.app.get("/average?X=1,2,3,4,5,6")
        self.assertEqual(b'3.5\n', respond.data)

        respond = self.app.get("/mean?X=2,3,4,6")
        self.assertEqual(b'3.75\n', respond.data)

        respond = self.app.get("/avg?X=2,3,4")
        self.assertEqual(b'3\n', respond.data)

        respond = self.app.get("/average?X=10,2.8,100")
        self.assertEqual(b'37.6\n', respond.data)

        respond = self.app.get("/mean?X=10,2.8,100")
        self.assertEqual(b'37.6\n', respond.data)

        respond = self.app.get("/avg?X=10,2.8,100")
        self.assertEqual(b'37.6\n', respond.data)

    def testing_minimum(self):
        # Test script for taking  maniumum value in a given input
        respond = self.app.get("/min?X=15,1,57,37,8,34,5")
        self.assertEqual(b'1\n', respond.data)

        respond = self.app.get("/min?X=1,2,45,7,0,7.5,3")
        self.assertEqual(b'0\n', respond.data)

    def testing_maximum(self):
        respond = self.app.get("/max?X=15,1,57,37,8,34,5")
        self.assertEqual(b'57\n', respond.data)

        respond = self.app.get("/max?X=1,2,45,7,0,7.5,3")
        self.assertEqual(b'45\n', respond.data)

    def testing_median(self):
        # Test the page with an empty route

        respond = self.app.get("/median?X=1,2,0,3,4,100")
        self.assertEqual(b'2.5 \n', respond.data)

        respond = self.app.get("/median?X=1,2,3,4,5,6")
        self.assertEqual(b'3.5 \n', respond.data)


if __name__ == "__main__":
    unittest.main()
© 2020 GitHub, Inc.
Terms
Privacy
