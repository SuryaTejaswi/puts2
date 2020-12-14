import unittest
import main

class AdvanceCalc(unittest.TestCase):

    
    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    
    
    def testing_minimum(self):

        #Test script for taking  maniumum value in a given input
        respond=self.app.get("/min?X=15,1,57,37,8,34,5")
        self.assertEqual(b'1\n',respond.data)

        respond=self.app.get("/min?X=1,2,45,7,0,7.5,3")
        self.assertEqual(b'0\n',respond.data)


if __name__ == "__main__":
    unittest.main()