import unittest
import main


class AdvanceCalc(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    def testing_median(self):
        # Test the page with an empty route

        respond = self.app.get("/median?X=1,2,0,3,4,100")
        self.assertEqual(b'2.5 \n', respond.data)

        respond = self.app.get("/median?X=1,2,3,4,5,6")
        self.assertEqual(b'3.5 \n', respond.data)


if __name__ == "__main__":
    unittest.main()